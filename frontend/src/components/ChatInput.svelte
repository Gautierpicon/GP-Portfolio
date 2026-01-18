<script>
  import { onMount, onDestroy } from "svelte";
  import gsap from "gsap";
  import { TextPlugin } from "gsap/TextPlugin";
  import prompts from '../data/prompts.json';

  gsap.registerPlugin(TextPlugin);

  export let onSend = null;
  export let disabled = false;
  export let dynamicPlaceholder = false;
  export let placeholder = "Send a message";

  let message = "";
  let textarea;
  let currentPlaceholder = placeholder;
  let typewriterTimeline;

  const autoResize = () => {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
  };

  const getRandomPrompt = (prevIndex) => {
    let newIndex;
    do {
      newIndex = Math.floor(Math.random() * prompts.length);
    } while (newIndex === prevIndex && prompts.length > 1);
    return { prompt: prompts[newIndex], index: newIndex };
  };

  const createTypewriterAnimation = () => {
    if (!dynamicPlaceholder || prompts.length === 0) return;

    typewriterTimeline = gsap.timeline({ repeat: -1 });

    let prevPromptIndex = -1;

    const addPromptAnimation = () => {
      const { prompt, index } = getRandomPrompt(prevPromptIndex);
      prevPromptIndex = index;
      let obj = { progress: 0 };

      typewriterTimeline
        .add(() => {
          obj.progress = 0;
        })
        .to(obj, {
          duration: prompt.length * 0.07,
          progress: 1,
          ease: "none",
          onUpdate: function () {
            const charIndex = Math.floor(this.targets()[0].progress * prompt.length);
            currentPlaceholder = prompt.substring(0, charIndex + 1);
          },
          onComplete: function () {
            currentPlaceholder = prompt;
          },
        })
        .to({}, { duration: 3 })
        .add(() => {
          obj.progress = 0;
        })
        .to(obj, {
          duration: prompt.length * 0.06,
          progress: 1,
          ease: "none",
          onUpdate: function () {
            const charIndex = Math.floor(this.targets()[0].progress * prompt.length);
            currentPlaceholder = prompt.substring(0, prompt.length - charIndex);
          },
          onComplete: function () {
            currentPlaceholder = "";
          },
        })
        .to({}, { duration: 0.5 });
    };

    addPromptAnimation();
    addPromptAnimation();
    addPromptAnimation();

    currentPlaceholder = "";
  };

  onMount(() => {
    autoResize();
    createTypewriterAnimation();
  });

  onDestroy(() => {
    if (typewriterTimeline) {
      typewriterTimeline.kill();
    }
  });

  const handleFocus = () => {
    if (typewriterTimeline) {
      typewriterTimeline.pause();
      currentPlaceholder = "";
    }
  };

  const handleBlur = () => {
    if (typewriterTimeline && !message.trim()) {
      typewriterTimeline.restart();
    }
  };

  const sendMessage = () => {
    const trimmed = message.trim();
    if (!trimmed) return;

    if (onSend) {
      onSend(trimmed);
      message = "";
      autoResize();
    } else {
      sessionStorage.setItem('initialMessage', trimmed);
      window.location.href = '/chat';
    }
  };

  const handleKeydown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };
</script>

<div class="w-full max-w-2xl bg-[#f7f7f7] rounded-3xl shadow-sm flex flex-col">
    <textarea
        bind:this={textarea}
        bind:value={message}
        placeholder={currentPlaceholder}
        rows="1"
        class="w-full min-h-12 bg-transparent resize-none outline-none border-none text-dark placeholder-gray-400 overflow-y-auto px-6 pt-6"
        style="max-height: 12rem;"
        on:input={autoResize}
        on:keydown={handleKeydown}
        on:focus={handleFocus}
        on:blur={handleBlur}
        disabled={disabled}
    ></textarea>

    <div class="flex justify-end px-2 py-2">
        <button
            on:click={sendMessage}
            disabled={disabled || message.trim() === ""}
            aria-label="Send message"
            class="w-9 h-9 rounded-full flex items-center justify-center transition
                {message.trim() === '' ? 'cursor-not-allowed bg-gray-200' :
                disabled ? 'cursor-wait bg-gray-400' :
                'cursor-pointer bg-black'}"
        >
            <svg 
                xmlns="http://www.w3.org/2000/svg" 
                fill="none"
                viewBox="0 0 24 24" 
                stroke-width="2.7"
                stroke="white"
                class="w-4 h-4"
                aria-hidden="true"
            >
                <path 
                stroke-linecap="round" 
                stroke-linejoin="round"
                d="M4.5 10.5 12 3m0 0 7.5 7.5M12 3v18" 
                />
            </svg>
        </button>
    </div>
</div>
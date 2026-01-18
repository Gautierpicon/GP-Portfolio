<script>
  import { onMount, onDestroy } from "svelte";
  import prompts from '../data/prompts.json';

  export let onSend = null;
  export let disabled = false;
  export let dynamicPlaceholder = false;
  export let placeholder = "Send a message";

  let message = "";
  let textarea;
  let currentPlaceholder = placeholder;
  let currentPromptIndex = 0;
  let placeholderInterval;

  const autoResize = () => {
    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";
  };

  const cyclePlaceholder = () => {
    let newIndex;
    do {
      newIndex = Math.floor(Math.random() * prompts.length);
    } while (newIndex === currentPromptIndex && prompts.length > 1);
    currentPromptIndex = newIndex;
    currentPlaceholder = prompts[currentPromptIndex];
  };

  onMount(() => {
    autoResize();
    if (dynamicPlaceholder && prompts.length > 0) {
      currentPlaceholder = prompts[0];
      placeholderInterval = setInterval(cyclePlaceholder, 4000);
    }
  });

  onDestroy(() => {
    if (placeholderInterval) {
      clearInterval(placeholderInterval);
    }
  });

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
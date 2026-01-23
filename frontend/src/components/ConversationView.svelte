<script>
  import { onMount } from "svelte";
  import gsap from 'gsap';
  import ChatInput from './ChatInput.svelte';

  import duckImage from '../assets/duck.webp';
  import thinkingDuckImage from '../assets/thinking-duck.webp';

  const BACKEND_URL = import.meta.env.PUBLIC_BACKEND_URL;

  let messages = [];
  let isLoading = false;
  let messagesContainer;
  let dot1, dot2, dot3;

  const scrollToBottom = () => {
    if (messagesContainer) {
      setTimeout(() => {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }, 100);
    }
  };

  onMount(() => {
    const initialMessage = sessionStorage.getItem('initialMessage');

    if (initialMessage) {
      sessionStorage.removeItem('initialMessage');
      handleSendMessage(initialMessage);
    }
  });

  $: if (isLoading && dot1) {
    gsap.to(dot1, { y: -5, duration: 0.5, ease: "power1.inOut", repeat: -1, yoyo: true });
    gsap.to(dot2, { y: -5, duration: 0.5, ease: "power1.inOut", repeat: -1, yoyo: true, delay: 0.2 });
    gsap.to(dot3, { y: -5, duration: 0.5, ease: "power1.inOut", repeat: -1, yoyo: true, delay: 0.4 });
  } else if (!isLoading) {
    gsap.killTweensOf([dot1, dot2, dot3]);
  }

  const handleSendMessage = async (messageText) => {
    messages = [...messages, { role: "user", content: messageText }];
    scrollToBottom();

    isLoading = true;

    messages = [...messages, { role: "assistant", content: "" }];
    const assistantIndex = messages.length - 1;

    try {
      const res = await fetch(`${BACKEND_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: messageText })
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { done, value } = await reader.read();
        
        if (done) break;

        const chunk = decoder.decode(value);
        
        messages[assistantIndex].content += chunk;
        messages = [...messages];
        
        scrollToBottom();
      }
    } catch (e) {
      console.error(e);
      messages[assistantIndex].content = `I'm broke, I don't have enough money to host the AI at the moment. Please come back later.\n\nIn the meantime, go to the project's GitHub page to explore the source code or even contribute if you feel like it: <a href="https://github.com/Gautierpicon/GP-Portfolio" target="_blank" rel="noopener noreferrer" class="underline">github.com/Gautierpicon/GP-Portfolio</a>`;
      messages = [...messages];
    } finally {
      isLoading = false;
    }
  };
</script>

<div class="min-h-screen flex flex-col">
  <div 
    bind:this={messagesContainer}
    class="flex-1 overflow-y-auto px-4 py-6 space-y-4"
  >
    {#if messages.length === 0}
      <div class="flex items-center justify-center h-full text-gray-600">
        <p>Start the conversation...</p>
      </div>
    {/if}

    {#each messages as msg, idx}
      {#if !(isLoading && idx === messages.length - 1 && msg.role === 'assistant' && msg.content === '')}
        <div class="flex {msg.role === 'user' ? 'justify-end' : 'justify-start'}">
          <div class="flex flex-col items-start {msg.role === 'assistant' ? 'pl-6 ml-0' : 'pr-6'}">
            <div 
              class="max-w-2xl rounded-3xl text-gray-800
                {msg.role === 'user' 
                ? 'px-4 py-2 bg-[#f7f7f7] shadow-sm' 
                : 'px-6 py-4 border bg-transparent'}"
            >
              <p class="whitespace-pre-wrap wrap-break-words wrap-anywhere">
                {@html msg.content || (msg.role === 'assistant' ? '\u200B' : '')}
              </p>
            </div>

            {#if msg.role === 'assistant' && idx === messages.length - 1}
              <div class="mt-3 flex">
                <img 
                  src={isLoading ? thinkingDuckImage.src : duckImage.src}
                  alt="Duck"
                  class="w-15 h-15 rounded-full bg-gray-200"
                />
              </div>
            {/if}
          </div>
        </div>
      {/if}
    {/each}

    {#if isLoading && messages[messages.length - 1]?.role === 'assistant' && messages[messages.length - 1]?.content === ''}
      <div class="flex justify-start">
        <div class="flex flex-col items-start pl-6">
          <div class="max-w-2xl rounded-3xl px-6 py-4 border bg-transparent">
            <div class="flex space-x-2">
              <div bind:this={dot1} class="w-2 h-2 bg-gray-500 rounded-full"></div>
              <div bind:this={dot2} class="w-2 h-2 bg-gray-500 rounded-full"></div>
              <div bind:this={dot3} class="w-2 h-2 bg-gray-500 rounded-full"></div>
            </div>
          </div>

          <div class="mt-3 flex">
            <img 
              src={thinkingDuckImage.src}
              alt="Duck thinking"
              class="w-15 h-15 rounded-full bg-gray-200"
            />
          </div>
        </div>
      </div>
    {/if}
  </div>

  <div class="bg-white p-4">
    <div class="max-w-2xl mx-auto">
      <ChatInput onSend={handleSendMessage} disabled={isLoading} />
    </div>
  </div>
</div>
<script>
  import { onMount } from "svelte";
  import ChatInput from './ChatInput.svelte';

  const BACKEND_URL = import.meta.env.PUBLIC_BACKEND_URL;

  let messages = [];
  let isLoading = false;
  let messagesContainer;

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

  const handleSendMessage = async (messageText) => {
    messages = [...messages, { role: "user", content: messageText }];
    scrollToBottom();

    isLoading = true;

    try {
      const res = await fetch(`${BACKEND_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: messageText })
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      if (data.response) {
        messages = [...messages, { role: "assistant", content: data.response }];
        scrollToBottom();
      } else {
        alert("No response received from the server");
      }
    } catch (e) {
      console.error(e);
      alert("Failed to send message. Make sure the backend is running at " + BACKEND_URL);
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
      <div class="flex items-center justify-center h-full text-gray-400">
        <p>Start the conversation...</p>
      </div>
    {/if}

    {#each messages as msg}
      <div class="flex {msg.role === 'user' ? 'justify-end' : 'justify-start'}">
        <div 
          class="max-w-2xl rounded-3xl text-gray-800
            {msg.role === 'user' 
              ? 'px-4 py-2 bg-[#f7f7f7] shadow-sm' 
              : 'px-6 py-4 bg-transparent'}"
        >
          <p class="whitespace-pre-wrap">{msg.content}</p>
        </div>
      </div>
    {/each}

    {#if isLoading}
      <div class="flex justify-start">
        <div class="max-w-2xl bg-white rounded-3xl px-6 py-4 shadow-sm">
          <div class="flex space-x-2">
            <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
            <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
            <div class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0.4s"></div>
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
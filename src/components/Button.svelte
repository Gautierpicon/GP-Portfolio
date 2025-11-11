<script>
  export let type = "button";
</script>

<button
  type={type}
  class="cursor-pointer px-4 py-2 rounded-lg font-medium transition bg-blue-600 text-white hover:bg-blue-700"
>
  <slot />
</button>

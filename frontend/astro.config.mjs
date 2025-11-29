// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from "@tailwindcss/vite";
import svelte from "@astrojs/svelte";

// https://astro.build/config
export default defineConfig({
  site: 'https://gp-portfolio-theta.vercel.app/',
  
  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [svelte()],

  output: 'static',
});
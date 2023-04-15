import adapter from '@sveltejs/adapter-auto';
import path from 'path';
import { vitePreprocess } from '@sveltejs/kit/vite';

const config = {
	preprocess: vitePreprocess(),
  kit: {
		adapter: adapter(),
  }
};

export default config;

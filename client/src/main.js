import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		"api_uri": "/api/v1"
	}
});

export default app;
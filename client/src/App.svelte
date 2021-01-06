<script>
	import Exponent from './Exponent.svelte';
	import Fibonacci from './Fibonacci.svelte';
	import Factorial from './Factorial.svelte';
	import Errors from './Errors.svelte';

	export let api_uri;
	const exponent_uri = `${api_uri}/exponent`;
	const fibonacci_uri = `${api_uri}/fibonacci`;
	const factorial_uri = `${api_uri}/factorial`;

	let exponent_result, fibonacci_result, factorial_result;
	let exponent_loading, fibonacci_loading, factorial_loading;
	let errors = {};

	function parse(json_string) {
		return JSON.parse(json_string.replace(/(["']?)(\d+)(["']?)/g, "\"$2\""));
	}

	async function computeExponent(e) {
		exponent_loading = true;
		const res = await fetch(exponent_uri, {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(e.detail)
		})
		
		const json = parse(await res.text());
		exponent_loading = false;
		if(res.ok) {
			errors = {};
			exponent_result = json.result;
		} else {
			errors = json.message;
		}
	};

	async function computeFibonacci(e) {
		fibonacci_loading = true;
		const res = await fetch(fibonacci_uri, {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(e.detail)
		})
		
		const json = parse(await res.text());
		fibonacci_loading = false;
		if(res.ok) {
			errors = {};
			fibonacci_result = json.result;
		} else {
			errors = json.message;
		}
	};

	async function computeFactorial(e) {
		factorial_loading = true;
		const res = await fetch(factorial_uri, {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(e.detail)
		})

		const json = parse(await res.text());
		factorial_loading = false;
		if(res.ok) {
			errors = {};
			factorial_result = json.result;
		} else {
			errors = json.message;
		}
	};
</script>

<main>
	<h1>Welcome to Mathapi!</h1>
	<Errors bind:errors={errors} />
	<Exponent on:value="{computeExponent}" bind:result={exponent_result} bind:loading="{exponent_loading}" />
	<Fibonacci on:value="{computeFibonacci}" bind:result={fibonacci_result} bind:loading="{fibonacci_loading}"  />
	<Factorial on:value="{computeFactorial}" bind:result={factorial_result} bind:loading="{factorial_loading}" />
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
<script>
  import { createEventDispatcher } from "svelte";
  export let result = "?";
  export let loading = false;

  const dispatch = createEventDispatcher();

  let number = 0;

  $: {
    number;
    result = "?";
  }

  function compute() {
    number = Math.floor(number);

    dispatch("value", { number });
  }
</script>

<style>
  div.main {
    border: 1px solid black;
    padding: 20px;
    word-wrap: break-word;
    white-space: pre-wrap;
    margin-bottom: 10px;
    min-height: 225px;
  }

  input {
    max-width: 100%;
  }

  .loading {
    width: 100%;
    text-align: center;
    line-height: 225px;
    height: 225px;
  }
</style>

<div class="main">
  {#if loading}
    <div class="loading">loading...</div>
  {:else}
  <h1>Compute nth fibonacci number:</h1>
  <input
    type="number"
    name="number"
    placeholder="number"
    step="1"
    bind:value={number} />
  <button on:click={compute}>Compute</button>
  <h3>fib({number}) = {result}</h3>
  {/if}
</div>

<script>
  import { createEventDispatcher } from "svelte";
  export let loading = false;

  const dispatch = createEventDispatcher();

  let number = 0;
  let email = "";

  function compute() {
    number = Math.floor(number);

    dispatch("value", { number, email });
    alert('You will receive the result on the provided email.')
    number = 0;
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
  <h1>Compute nth fibonacci number and receive result by email:</h1>
  <input
    type="number"
    name="number"
    placeholder="number"
    step="1"
    bind:value={number} />
  <input
    type="email"
    name="email"
    placeholder="email"
    bind:value={email} />
  <button on:click={compute}>Compute</button>
  {/if}
</div>

<script>
  import { createEventDispatcher } from "svelte";
  export let result = "?";
  export let loading = false;

  const dispatch = createEventDispatcher();

  let base = 0;
  let exponent = 1;

  $: {
    base, exponent;
    result = "?";
  }

  function compute() {
    base = Math.floor(base);
    exponent = Math.floor(exponent);

    dispatch("value", { base, exponent });
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
  <h1>Compute the power:</h1>
  <input
    type="number"
    name="base"
    placeholder="base"
    step="1"
    bind:value={base} />
  <input
    type="number"
    name="base"
    placeholder="exponent"
    step="1"
    bind:value={exponent} />
  <button on:click={compute}>Compute</button>
  <h3>{base}<sup>{exponent}</sup> = {result}</h3>
  {/if}
</div>

<script>
  export let errors = {};
</script>

<style>
  ul {
    border: 1px solid red;
    color: red;
    padding: 20px;
    margin-bottom: 10px;
  }
</style>

{#if Object.entries(errors).length > 0 }
<ul>
  {#each Object.entries(errors) as [field, error] (field)}
  <li><strong>{field}: </strong>{error}</li>
  {/each}
</ul>
{/if}

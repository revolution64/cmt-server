<template>
    <p class="about-paragraph">Deze webapp gebruikt Natural Language Processing technieken om een corpus om te zetten naar POS (part of speech) en lemmas (kernwoorden). Vervolgens worden combinaties van die data gebruikt om synoniemen voor te stellen via de lexicale database van OpenDutchWordNet.</p>
    <p class="about-paragraph">Om de tekst via NLP technieken om te zetten naar POS en Lemma, werden modellen van <a href="https://spacy.io/">spacy</a> gebruikt</p>
    <p class="about-paragraph">Om de synoniemen voor te stellen, werd een lichtjes aangepaste versie van de Python module <a href="https://github.com/cltl/OpenDutchWordnet">OpenDutchWordnet</a> gebruikt </p>
    <p class="about-paragraph">Synoniemenzoeker werkt voorlopig enkel voor werkwoorden, bijvoeglijke en zelfstandige naamworden</p>
</template>

<style>

  .about-paragraph {
    padding: 1rem 0rem;
  }

</style>

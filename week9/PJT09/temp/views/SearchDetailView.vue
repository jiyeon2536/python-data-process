<template>
  <div>
    <h1>동영상 상세 페이지</h1>
    <div class="video-list">
      {{ video }}
      <hr />
      {{ video.id.videoId }}
      <hr />
      {{ video.snippet.title }}
      <iframe
        id="ytplayer"
        type="text/html"
        width="720"
        height="405"
        frameborder="0"
        :src="videoSrc"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const route = useRoute();

const video = ref([]);
const videoId = route.params.videoId;
const videoSrc = `https://www.youtube.com/embed/${videoId}`;

axios
  .get(apiURL)
  .then((response) => {
    video.value = response.data;
  })
  .catch((error) => {
    console.log(error);
  });
</script>

<style scoped></style>

<template>
  <div>
    <h1>메인 페이지</h1>
    <input @keyup.enter="search" type="text" v-model="keywords" />
    <div class="video-list">
      <div v-for="video in videos.items" :key="video.id" class="video-card">
        <img :src="video.snippet.thumbnails.default.url" alt="">
        {{ video.snippet.title }}
        <hr>
        {{ video.snippet.description }}
        <hr>
        <button @click="goDetail(video)">상세페이지로 이동</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
const router = useRouter()
const videos  = ref([])
const apikey = 'AIzaSyBUXWa4S5ZsG8uvNMzYExiS9OLyOltMa8A'
const keywords = ref("");

const goDetail = (video) => {
  router.push(`/${video.id.videoId}`);
};

const search = function () {
  const storeURL = `https://www.googleapis.com/youtube/v3/search?key=${apikey}&part=snippet&type=video&q=${keywords.value}`;
  console.log(storeURL); // URL 확인
  axios.get(storeURL)
    .then((response) => {
      console.log(response.data);
      videos.value = response.data;
    }).catch((error) => {
      console.error(error);
    })
};

</script>

<style scoped>
.video-list {
display: flex;
flex-wrap: wrap;
gap: 10px;
}

.video-card {
border: 1px solid #000;
width: 200px;
}

.video-card img {
width: 200px;
height: 200px;
object-fit: fill;
}
</style>


<!-- <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark"> -->
<!-- </nav> -->
<template>
  <div>
    <h1>메인 페이지</h1>
    <div v-if="!productIsEmpty" class="product-list">
      <div v-for="product in products" :key="product.id" class="product-card">
        <img :src="product.image" alt="" />
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="addCart(product)">장바구니에 추가</button>
      </div>
    </div>
    <div v-else>
      <strong>로딩중</strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const products = ref([]);
const storeURL = "https://fakestoreapi.com/products";
const router = useRouter();

axios
  .get(storeURL)
  .then((response) => {
    // console.log(response.data);
    products.value = response.data;
  })
  .catch((error) => {
    console.log(error);
  });

const productIsEmpty = computed(() => {
  return products.value.length === 0 ? true : false;
});

const goDetail = (product) => {
  router.push(`/${product.id}`);
};

const addCart = (product) => {
  // 하나의 데이터만 저장 - 문제점: 덮어쓰기됨
  //   localStorage.setItem("cart", JSON.stringify(product));

  // 여러 데이터 저장
  // 현재 local storage 에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem("cart")) || [];
  // 중복된 제품이 있는지 확인
  const isDuplicate =
    existingCart.length > 0 &&
    existingCart.find((item) => item.id === product.id);

  // 중복이 아니라면 추가
  if (!isDuplicate) {
    alert("장바구니에 추가합니다");
    existingCart.push(product);
  } else {
    alert("이미 있는 상품입니다. 장바구니로 이동합니다");
  }

  // 수정된 카트 데이터를 localStorage 저장
  localStorage.setItem("cart", JSON.stringify(existingCart));

  router.push("/cart");
};
</script>

<style scoped>
.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.product-card {
  border: 1px solid black;
  width: 200px;
}
.product-card img {
  width: 200px;
  object-fit: fill;
}
</style>

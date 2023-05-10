<template>
  <div>  
    <p v-if='!imgSrc'> {{message}} </p>
    <img v-if='imgSrc' :src="imgSrc" alt="" style = 'height:500px;'>
    <br>
    <button @click='getCat'> Get Cat</button>
  </div>

</template>

<script>
import axios from 'axios'

export default {
    name: 'CatCome',
    data(){
        return{
            imgSrc: null,
            message: "짱기여운고양이로딩중",
        }
    },
    methods:{
        getCat: function(){
            const API_URL = "https://api.thecatapi.com/v1/images/search"
            axios.get(API_URL)
            .then((response) =>{
                const imgUrl = response.data[0].url
                this.imgSrc = imgUrl
                console.log("이미지 소스:" + imgUrl)
            })
        }
    }


}
</script>

<style>

</style>
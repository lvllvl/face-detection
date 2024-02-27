<template>
  <div class="video-container">
    <video ref="videoElement" width="640" height="480" autoplay></video>
    <div class="button-container">
      <button @click="activateCamera">Activate Camera</button>
      <button @click="HOG">HOG Camera</button>
      <button @click="HaarCascades">Haar Cascades Camera</button>
      <!-- Add more buttons for algorithm selection here -->
    </div>
  </div>
</template>

<style scoped>
.video-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button-container {
  margin-top: 10px;
}
</style>

<script>
export default {
  data() {
    return {
      stream: null,
    };
  },
  methods: {
    async activateCamera() {
      if (!this.stream) {
        try {
          // Request camera access
          this.stream = await navigator.mediaDevices.getUserMedia({ video: true });
          this.$refs.videoElement.srcObject = this.stream;
        } catch (error) {
          console.error('Error accessing the camera', error);
          this.stream = null;
        }
      } else {
        // Stop each track of the stream
        this.stream.getTracks().forEach(( track ) => track.stop() );
        this.stream = null;
      }
    },
  },
};
</script>

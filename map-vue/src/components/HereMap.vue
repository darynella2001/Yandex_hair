<template>
  <div id="map">
  <!--In the following div the HERE Map will render-->
    <div id="mapContainer" style="height:600px;width:100%" ref="hereMap"></div>
  </div>
</template>

<script>
export default {
  name: "HereMap",
  props: {
    center: Object,
  },
  data() {
    return {
      platform: null,
      apikey: "5TOoQM4VPWiJ2aL47FK5XbcJFCivpBGP4Yo2UEsxcwI"
      // You can get the API KEY from developer.here.com
    };
  },
  async mounted() {
    // Initialize the platform object:
    const platform = new window.H.service.Platform({
      apikey: this.apikey
    });
    this.platform = platform;
    this.initializeHereMap();
  },
  methods: {
    initializeHereMap() { // rendering map
      function addMarkersToMap(map) {
    var marker1 = new H.map.Marker({lat:47.02, lng:28.85});
    map.addObject(marker1);

    var marker2 = new H.map.Marker({lat:47.01, lng: 28.84});
    map.addObject(marker2);

    var marker3 = new H.map.Marker({lat:47.04, lng:28.86});
    map.addObject(marker3);

    var marker4 = new H.map.Marker({lat:47.02, lng: 28.83});
    map.addObject(marker4);

    var marker5 = new H.map.Marker({lat:47.00, lng:28.82});
    map.addObject(marker5);
}

      const mapContainer = this.$refs.hereMap;
      const H = window.H;
      // Obtain the default map types from the platform object
      var maptypes = this.platform.createDefaultLayers();

      // Instantiate (and display) a map object:
      var map = new H.Map(mapContainer, maptypes.vector.normal.map, {
        zoom: 12.7,
        center: this.center,
        pixelRatio: window.devicePixelRatio || 1
      });

      addEventListener("resize", () => map.getViewPort().resize());

      // add behavior control
      new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

      // add UI
      H.ui.UI.createDefault(map, maptypes);
      // End rendering the initial map
      window.onload = function () {
        addMarkersToMap(map);
      }
    }
  }
};
</script>

<style scoped>
#map {
  width: 60vw;
  min-width: 360px;
  text-align: center;
  margin: 5% auto;
  background-color: #ccc;
}
</style>
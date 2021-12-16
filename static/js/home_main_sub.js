
new Vue({
    el: '.js-home_main_sub',
    data: {
      current: 0,
      slides: [],
      speed: 3000,
      timer: null
    },
    methods: {
      startRotation: function () {
        this.timer = setInterval(this.next, this.speed);
      },
      stopRotation: function () {
        clearTimeout(this.timer);
        this.timer = null;
      },
      next: function () {
        var current = this.current;
        var next = current + 1;
  
        if (next > this.slides.length - 1) {
          next = 0;
        }
        this.current = next;
        this.setActive(this.current);
      },
      prev: function () {
        var current = this.current;
        var prev = current - 1;
  
        if (prev < 0) {
          prev = this.slides.length -1;
        }
  
        this.current = prev;
        this.setActive(this.current);
      },
      isActive: function (slide) {
        return this.current === slide;
      },
      setActive: function (slide) {
        this.current = slide;
      },
    },
    created: function () {
      axios.get(jsonpath)
      .then(function (response) {
        this.slides = response.data.slides
      }.bind(this))
      .catch(function (error) {
        console.log(error);
      });
    },
    mounted: function () {
      this.startRotation();
    }
  });
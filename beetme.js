self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open("beetme-offline").then(function(cache) {
      return cache.addAll(
        [
          '/beetme.html',
          '/beetme.js',
          '/beetme.png',
          '/beetme.json'
        ]
      );
    })
  );
});

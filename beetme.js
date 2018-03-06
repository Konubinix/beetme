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

self.addEventListener('fetch', function(event) {
	event.respondWith(
		caches.open('beetme-offline').then(
			function(cache) {
				return cache.match(event.request).then(function (response) {
					return response || fetch(event.request).then(function(response) {
						if(
							event.request.url.match(new RegExp("/beetme.html|/beetme.png|/beetme.json"))
						  )
						{
							cache.put(event.request, response.clone());
						}
						return response;
					});
				});
			})
	);
});

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from flexx import app, ui, event, config
from flexx.pyscript import RawJS
import os


def add_asset(name, path):
    if path.endswith(".png"):
        app.assets.add_shared_data(
            name,
            open(path, "rb").read()
        )
    else:
        app.assets.associate_asset(
            __name__,
            name,
            open(path, "rb").read().decode(),
        )


# add_asset(
#     "bluebird.min.js",
#     os.path.join(
#         os.path.dirname(__file__),
#         "bower_components",
#         "bluebird",
#         "js",
#         "browser",
#         "bluebird.min.js"),
# )

add_asset(
    "pouchdb-6.3.4.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "pouchdb",
        "dist",
        "pouchdb.min.js"),
)

add_asset(
    "moment-with-locales.min.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "moment",
        "min",
        "moment-with-locales.min.js",
    )
)

add_asset(
    "jquery-3.2.1.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "jquery",
        "dist",
        "jquery.min.js"),
)

add_asset(
    "jquery.dataTables.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net",
        "js",
        "jquery.dataTables.min.js"),
)

add_asset(
    "jquery.dataTables.css",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-dt",
        "css",
        "jquery.dataTables.css"),
)

add_asset(
    "dataTables.select.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-select",
        "js",
        "dataTables.select.min.js"),
)

add_asset(
    "dataTables.select.css",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-select-dt",
        "css",
        "select.dataTables.css"),
)

add_asset(
    "dataTables.rowReorder.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-rowreorder",
        "js",
        "dataTables.rowReorder.min.js"),
)

add_asset(
    "dataTables.rowReorder.css",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-rowreorder-dt",
        "css",
        "rowReorder.dataTables.css"),
)

add_asset(
    "dataTables.buttons.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-buttons",
        "js",
        "dataTables.buttons.min.js"),
)

add_asset(
    "buttons.dataTables.css",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "datatables.net-buttons-dt",
        "css",
        "buttons.dataTables.css"),
)

add_asset(
    "toastr.min.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "toastr",
        "toastr.min.js"),
)

add_asset(
    "toastr.min.css",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "toastr",
        "toastr.min.css"),
)

add_asset(
    "dataTables.row.show.js",
    os.path.join(
        os.path.dirname(__file__),
        "assets",
        "dataTables.row.show.js"),
)

add_asset(
    "cookie.min.js",
    os.path.join(
        os.path.dirname(__file__),
        "bower_components",
        "cookie",
        "cookie.min.js"),
)


class BeetMe(ui.VBox):
    CSS = """
.flx-BeetMe {
    //overflow: visible;
    margin: 5px;
}
.label {
background-color: none;
border-style: none;
font-weight: bold;
}

body {
//background-color: #4682b4;
//background-color: #87ceeb;
background-color: PaleTurquoise;
background-color: WhiteSmoke;
background-color: #dcf1ff;
}

.p-TabBar-tabLabel{
font-size: 2em;
}

.date {
padding-top: 3em;
}

.table {
overflow: scroll;
}

.total {
padding: 1em;
}
"""
    def init(self):
        def head_table(table):
            with table:
                with ui.html.thead():
                    with ui.html.tr():
                        ui.html.th(text="track")
                        ui.html.th(text="title")
                        ui.html.th(text="album")
                        ui.html.th(text="artist")
                with ui.html.tfoot():
                    with ui.html.tr():
                        ui.html.th(text="track")
                        ui.html.th(text="title")
                        ui.html.th(text="album")
                        ui.html.th(text="artist")

        self.progress = ui.ProgressBar(value=0, flex=0, style="display: none;")
        with ui.TabPanel(flex=0.9) as self.tab:
            with ui.HBox(title="Search") as self.search_widget:
                with ui.VBox(flex=0.3):
                    ui.Label(
                        style="font-size: 0.5em;",
                        text="A and B => A/B; A or B => A , B")
                    with ui.HBox(flex=0.1):
                        ui.Label(text="Query", flex=0)
                        self.search_query = ui.LineEdit(text="", flex=1)
                    self.search_button = ui.Button(text="Search", flex=0.5)
                    with ui.HBox(flex=0.5):
                        self.put_to_cache = ui.Button(text="Put to cache")
                        self.select_all = ui.Button(text="Select all")
                        self.select_none = ui.Button(text="Select none")
                with ui.Layout(css_class="table", flex=0.7):
                    self.search_results = ui.html.table()
                    head_table(self.search_results)

            with ui.HBox(title="Play"):
                with ui.VBox(flex=0.3):
                    with ui.HBox():
                        ui.Label(text="cache", flex=0)
                        self.cache_list = ui.ComboBox(
                            editable=True,
                            flex=1
                        )
                    with ui.HBox(flex=0.1):
                        self._reset_cache = ui.Button(text="Reset cache", flex=0.2)
                        self.remove = ui.Button(text="Remove", flex=0.1)
                    with ui.HBox(flex=1):
                        self.play_button = ui.Button(text="Play selected", flex=0.2)
                        self.show_button = ui.Button(text="Show", flex=0.1)
                    with ui.HBox(flex=0.1):
                        self.toggle_button = ui.ToggleButton(text="Play", flex=0.2)
                        self.shuffle_button = ui.ToggleButton(text="Random", flex=0.2)
                    with ui.HBox(flex=0.2):
                        self.prev_button = ui.Button(text="<<-", flex=0.7)
                        self.seekbackward_button = ui.Button(text="<-", flex=0.2)
                        self.seekforward_button = ui.Button(text="->", flex=0.2)
                        self.next_button = ui.Button(text="->>", flex=0.7)
                with ui.Layout(css_class="table", flex=0.7):
                    self.cache = ui.html.table(flex=0.5)
                    head_table(self.cache)
            with ui.FormLayout(title="Cache"):
                self.clear_cache = ui.Button(text="Remove cache", flex=0)
            with ui.FormLayout(title="Config"):
                self.update = ui.Button(text="Update", flex=1)
                self._beet_url = ui.LineEdit(title="Beet url")
                self._beet_username = ui.LineEdit(title="Username")
                self._beet_password = ui.LineEdit(title="Password", password_mode=True)
        with ui.HBox(flex=0):
            self.audio = ui.html.audio(flex=1)
        with ui.HBox(flex=0):
            self.time_min = ui.Label(text="15", flex=0.1)
            ui.Label(text="min", flex=0.1)
            self.time_sec = ui.Label(text="00", flex=0.1)
            ui.Label(text="s", flex=0.1)
            self.timeminus = ui.Button(text="-1", flex=0.5)
            self.timeplus = ui.Button(text="+1", flex=0.5)
            self.run_timer = ui.ToggleButton(text="Run", flex=0.5)
            self.timereset = ui.Button(text="Reset", flex=0.5)

    class JS:
        @event.connect("timeplus.mouse_click")
        def _timeplus(self, *evs):
            self.time_min.text = parseInt(self.time_min.text) + 1

        @event.connect("timeminus.mouse_click")
        def _timeminus(self, *evs):
            self.time_min.text = parseInt(self.time_min.text) - 1

        @event.connect("timereset.mouse_click")
        def _timereset(self, *evs):
            self.run_timer.checked = False
            self.time_min.text = "15"
            self.time_sec.text = "00"

        @event.connect("run_timer.checked")
        def _run_timer(self, *evs):
            if self.run_timer.checked:
                if not self.audio.node.paused:
                    self.start_timer()
            else:
                if self.run_timer_interval:
                    clearInterval(self.run_timer_interval)

        @event.connect("tab.current")
        def _tab_current(self, *evs):
            if self.inited == None:
                return
            ev = evs[-1]
            value = ev.new_value.title
            cookie.set("tab.current", value)

        @event.connect("_beet_url.text")
        def _beet_url_text(self, *evs):
            if self.inited == None:
                return
            ev = evs[-1]
            cookie.set("beet_url", self._beet_url.text)

        @event.connect("_beet_username.text")
        def _beet_username_text(self, *evs):
            if self.inited == None:
                return
            ev = evs[-1]
            cookie.set("beet_username", self._beet_username.text)

        @event.connect("_beet_password.text")
        def _beet_password_text(self, *evs):
            if self.inited == None:
                return
            ev = evs[-1]
            cookie.set("beet_password", self._beet_password.text)

        @event.connect("toggle_button.checked")
        def _toggle(self, *evs):
            if self.toggle_button.checked:
                self.audio.node.play()
            else:
                self.audio.node.pause()

        @event.connect("select_all.mouse_click")
        def _select_all(self, *evs):
            self.search_table.rows({"filter": "applied"}).select()

        @event.connect("select_none.mouse_click")
        def _select_none(self, *evs):
            self.search_table.rows().deselect()

        @event.connect("play_button.mouse_click")
        def _play_cache(self, *evs):
            id = self.cache_table.row({"selected": True}).id()
            self.play_cache_url(id)

        def load_cache(self):
            id = self.cache_table.row({"selected": True}).id()
            self.load_cached_url(id)

        def play_cache_url(self, url):
            if cookie.get("current_song_id") != url:
                cookie.remove("current_time")
            cookie.set("current_song_id", url)
            self.load_cached_url(
                url
            ).then(
                lambda : self.focus_selected()
            ).then(
                lambda : self.audio.node.play()
            ).catch(alert)

        def beet_url(self, query):
            url = self._beet_url.text
            if not url.endswith("/"):
                url = url + "/"
            l = document.createElement("a")
            url = url + query
            url = RawJS("""url.replace(new RegExp(" , ", "g"), "/,/")""")
            l["href"] = url
            return l.href

        @event.connect("put_to_cache.mouse_click")
        def _put_to_cache(self, *evs):
            urls = self.search_table.rows({"selected": True}).ids().toArray()
            for url in urls:
                dbval = [r for r in self._results if r["url"] == url][0]
                dbval["_id"] = url
                self.db.put(dbval)

            self.toastr_info("Caching " + urls.length.toString() + " musics")
            self.put_to_cache.disabled = True
            self.done_cache = 0
            self.progress.style = "display: block;"

            def update_progress():
                self.done_cache = self.done_cache + 1
                self.progress.value = self.done_cache / urls.length

            def add_to_cache(args):
                cache, keys = args
                promises = []
                cached_urls = [key.url for key in keys]
                urls_to_cache = []
                for url in urls:
                    if url in cached_urls:
                        update_progress()
                        def inform(obj):
                            self.toastr_info(obj["title"] + " already cached")
                        self.db.get(url).then(inform).catch(alert)
                    else:
                        urls_to_cache.append(url)

                # chain the fetches sequentially
                def pop_url_to_cache():
                    if not urls_to_cache:
                        done()
                        return
                    url = urls_to_cache.pop(0)
                    def closure_cache_put(url):
                        def cache_put(resp):
                            return cache.put(url, resp)
                        return cache_put
                    self.beet_fetch(url).then(closure_cache_put(url)).then(update_progress).then(pop_url_to_cache).catch(alert)
                return pop_url_to_cache()

            def done():
                self.put_to_cache.disabled = False
                self.progress.value = 0
                self.reset_cache()
                self.init_cache_list()
                self.progress.style = "display: none;"

            cache_promise = caches.open(self.cache_list.text)
            keys_promise = cache_promise.then(
                lambda cache: cache.keys()
            )
            Promise.all(
                [
                    cache_promise,
                    keys_promise,
                ]
            ).then(
                add_to_cache
            ).catch(
                alert
            )

        @event.connect("search_button.mouse_click")
        def __do_search(self, *evs):
            self.toastr_info("Searching")
            def get_json(resp):
                return resp.json()
            def create_buttons(json):
                data = []
                columns = [
                    {"data": "track"},
                    {"data": "title"},
                    {"data": "album"},
                    {"data": "artist"},
                ]
                self._results = json["results"]
                for res in self._results:
                    res["url"] = self.beet_url("item/" + res["id"] + "/file")
                for res in json["results"]:
                    data.append(
                        {
                            "DT_RowId": self.beet_url("item/" + res["id"] + "/file"),
                            "track": res["track"],
                            "title": res["title"],
                            "album": res["album"],
                            "artist": res["artist"],
                        }
                    )
                if navigator.userAgent.match(RegExp("Android", "i")):
                    select_style = "multi"
                else:
                    select_style = "os"

                self.search_table = jQuery(self.search_results.node).DataTable(
                    {
                        "data": data,
                        "columns": columns,
                        "rowReorder": True,
                        "select": {
                            "style": select_style,
                        },
                        "lengthMenu": [[50, 100, 200, -1], [50, 100, 200, "All"]],
                    }
                )
            if self.search_table != None:
                self.search_table.destroy()
                self.search_results.node.innerHTML = ""

            self.beet_fetch_query("item/query/" + self.search_query.text).then(get_json).then(create_buttons).catch(alert)

        def beet_fetch_query(self, query):
            url = self.beet_url(query)
            return self.beet_fetch(url)

        def beet_fetch(self, url):
            headers = {}
            if self._beet_username.text != "":
                headers['Authorization'] = 'Basic ' + btoa(self._beet_username.text + ":" + self._beet_password.text)
            def error_catch(err):
                alert("Failed to process url: " + url)
                window.err = err
                return Promise.reject(err)
            return fetch(
                url,
                {
                    "headers": Headers(headers),
                    "credentials": "include",
                }
            ).catch(error_catch)

        @event.connect('search_query.text')
        def _search_query(self, *evs):
            if self.inited == None:
                return
            cookie.set("search_query", self.search_query.text)

        @event.connect("show_button.mouse_click")
        def focus_selected(self, *evs):
            self.cache_table.row({"selected": True}).show().draw("page")
            self.cache_table.row({"selected": True}).node().scrollIntoView()

        def up_timer(self):
            now = moment()
            if now > self.end_time:
                self.audio.node.pause()
                self._timereset()
            else:
                duration = moment.duration(self.end_time - now)
                self.time_min.text = duration.minutes()
                self.time_sec.text = duration.seconds()

        def load_cached_url(self, url):
            def set_mediadata(obj):
                navigator.mediaSession.metadata = MediaMetadata({
                    "title": obj["title"],
                    "artist": obj["artist"],
                    "album": obj["album"],
                    "artwork": [
                        {
                            "src": self.beet_url("album/" + obj["album_id"] + "/art"),
                        },
                    ]
                })
            def update_track(obj):
                if navigator.mediaSession != None:
                    set_mediadata(obj)
            self.db.get(url).then(update_track).catch(alert)

            def load_blob(blob):
                url = window.URL.createObjectURL(blob)
                self.audio.node.pause()
                self.audio.node["src"] = url
                self.audio.node.load()
                current_time = cookie("current_time")
                if current_time != None:
                    self.audio.node.currentTime = current_time

            return caches.open(self.cache_list.text).then(
                lambda cache: cache.match(url)
            ).then(
                lambda resp: resp.blob()
            ).then(
                load_blob
            )

        @event.connect("search_query.key_press")
        def _do_search(self, *evs):
            ev = evs[-1]
            if ev.key == "Enter":
                self.search_button.node.click()

        def get_path(self, url):
            l = document.createElement("a")
            l["href"] = url
            return l.pathname

        @event.connect("_reset_cache.mouse_click")
        def reset_cache(self, *evs):
            self.cache.node.innerHTML = ""

            def create_table(r):
                data_dict = []
                for r in r["results"]:
                    data_dict.append(r["docs"][0]["ok"])
                columns = [
                    {"data": "track"},
                    {"data": "title"},
                    {"data": "album"},
                    {"data": "artist"},
                ]
                data = [
                    {
                        "DT_RowId": res["_id"],
                        "track": res["track"],
                        "title": res["title"],
                        "album": res["album"],
                        "artist": res["artist"],
                    }
                    for res in data_dict
                ]
                self.cached_data = data
                if self.cache_table != None:
                    self.cache_table.destroy()
                self.cache_table = jQuery(self.cache.node).DataTable(
                    {
                        "data": data,
                        "columns": columns,
                        "rowReorder": True,
                        "select": {
                            "style": "single",
                        },
                        "lengthMenu": [[50, 100, 200, -1], [50, 100, 200, "All"]],
                    }
                )
                selff = self
                def select_n_play(self):
                    selff.play_cache_url(selff.cache_table.row(self).id())

                jQuery(self.cache.node).on(
                    "dblclick",
                    "tr",
                    select_n_play,
                )
                if data != []:
                    selected_row_id = cookie.get("selected_row")
                    if selected_row_id != None:
                        selected_row = self.cache_table.row(
                            "*[id='" + selected_row_id + "']"
                        )
                    if selected_row_id == "" or selected_row == None or selected_row.count() == 0:
                        selected_row = self.cache_table.rows({"filter": "applied"})
                    selected_row.select()

                def on_select(e, dt, type, indexes):
                    if type == 'row':
                        cookie.set("selected_row", dt.row(indexes[0]).id())

                self.cache_table.on('select', on_select)
                self.toastr_info("Cache reset")
                self.focus_selected()
                if cookie.get("current_time"):
                    self.load_cache()

            def get_db_info(keys):
                paths = [
                    k.url
                    for k in keys
                ]
                return self.db.bulkGet(
                    {
                        "docs": [
                            {
                                "id": path,
                            }
                            for path in paths
                        ]
                    }
                )


            caches.open(self.cache_list.text).then(
                lambda cache: cache.keys()
            ).then(
                get_db_info
            ).then(
                create_table
            )

        def reload(self):
            window.location.reload(True)

        @event.connect("clear_cache.mouse_click")
        def _clear_cache(self):
            if confirm("Really removing the cache?"):
                cookie.remove("current_cache")
                caches.delete(
                    self.cache_list.text
                ).then(
                    self.clean_db
                ).then(
                    self.reload
                )

        def db_remove(self, url):
            def db_remove(obj):
                return self.db.remove(obj)
            return self.db.get(url).then(db_remove)

        @event.connect("remove.mouse_click")
        def _remove(self):
            def delete_cache(cache):
                promises = []
                ids = [
                    id
                    for id in
                    self.cache_table.rows({"selected": True}).ids().toArray()
                ]
                for id in ids:
                    url = self.beet_url("item/" + id + "/file")
                    promises.append(cache.delete(url))
                    promises.append(self.db_remove(url))
                return Promise.all(promises)

            if confirm("Remove for sure?"):
                caches.open(self.cache_list.text).then(
                    delete_cache
                ).then(
                    self.select_near
                ).then(
                    self.reset_cache
                ).catch(
                    alert
                )

        def start_db(self):
            self.db = PouchDB(self.cache_list.text, {})
            window.db = self.db

        @event.connect("cache_list.text")
        def change_cache(self, *evs):
            if self.inited:
                cookie.set("current_cache", self.cache_list.text)
                self.setup_db().then(
                    self.reset_cache
                )

        def setup_db(self, *ev):
            if self.db != None:
                return self.db.close().then(
                    self.start_db
                )
            else:
                def promise(resolve, reject):
                    self.start_db()
                    resolve("OK")
                return Promise(promise)

        def clean_db(self):
            if self.db != None:
                return self.db.destroy().then(
                    self.start_db
                )
            else:
                return self.start_db()

        @event.connect("update.mouse_click")
        def _update(self):
            cache_promise = caches.open("beetme-offline")
            keys_promise = cache_promise.then(
                lambda cache: cache.keys()
            )
            Promise.all(
                [
                    cache_promise,
                    keys_promise,
                ]
            )
            Promise.all(
                [
                    cache_promise,
                    keys_promise,
                ]
            ).then(
                lambda args: Promise.all(
                    [
                        args[0].delete(k)
                        for k in args[1]
                    ]
                )
            ).then(
                self.reload
            ).catch(
                alert
            )

        def toastr_warn(self, message):
            toastr.flush()
            toastr.warning(
                message.toString(),
                {"timeOut": 3000},
            )

        def toastr_info(self, message):
            toastr.flush()
            toastr.info(
                message.toString(),
                {"timeOut": 3000},
            )

        def setup_skewer(self):
            skewer = window.document.createElement('script')
            #skewer["src"] = "http://192.168.2.2:8080/skewer"
            skewer["src"] = "http://0.0.0.0:8080/skewer"
            window.document.head.appendChild(skewer)

        @event.connect("shuffle_button.checked")
        def _shuffle_checked(self, *evs):
            if self.inited == None:
                return
            cookie.set("random", self.shuffle_button.checked)

        def setup_meta(self):
            meta = document.createElement("meta")
            meta["name"] = "viewport"
            meta["content"] = "width=device-width"
            meta["initial-scale"] = 1.0
            meta["maximum-scale"] = 1.0
            meta["user-scalable"] = 0
            window.document.head.appendChild(meta)

        def init_cache_list(self):
            def closure_inited(inited):
                def _init_cache_list(names):
                    if "beetme-offline" in names:
                        names.remove("beetme-offline")
                    if not "default" in names:
                        names = ["default"] + names
                    self.cache_list.options = names
                    if not inited:
                        self.cache_list.text = cookie.get("current_cache") or names[0]
                window.caches.keys().then(
                    _init_cache_list
                ).catch(alert)
            closure_inited(self.inited)

        def debug_promise(self):
            Promise.config(
                {
                    "warnings": True,
                    "longStackTraces": True,
                    "cancellation": True,
                    "monitoring": True,
            })

        def init(self):
            # PouchDB.debug.enable('*')
            cookie.defaults.expires = 7
            # self.debug_promise()
            def init_post():
                tab_current = cookie.get("tab.current")
                if tab_current != None:
                    for child in self.tab.children:
                        if child.title == tab_current:
                            self.tab.current = child
                            break
                random = cookie.get("random")
                if random == "true":
                    self.shuffle_button.checked = True
                beet_url = cookie("beet_url")
                if beet_url == None:
                    self._beet_url.text = prompt("Please give me the url to beet web")
                    alert("The beet web url may be changed in the config tab")
                else:
                    self._beet_url.text = beet_url
                    cookie.set("beet_url", beet_url)
                beet_username = cookie.get("beet_username")
                if beet_username != None:
                    self._beet_username.text = beet_username
                beet_password = cookie.get("beet_password")
                if beet_password != None:
                    self._beet_password.text = beet_password
                self.search_query.text = cookie.get("search_query") or ""
                self.init_cache_list()
                self.inited = True

            setTimeout(init_post, 0)
            self.setup_meta()
            manifest = window.document.createElement('link')
            manifest["rel"] = 'manifest'
            manifest["href"] = "/beetme.json"
            document.getElementsByTagName('head')[0].appendChild(manifest)
            navigator.serviceWorker.register("/beetme.js").catch(self.toastr_warn)
            # self.setup_skewer()
            self.audio.node.controls = True
            toastr.options.positionClass = "toast-bottom-right"
            toastr.flush = toastr.clear
            self.skipTime = 10
            if navigator.mediaSession != None:
                navigator.mediaSession.setActionHandler('play', self.play)
                navigator.mediaSession.setActionHandler('pause', self.pause)
                navigator.mediaSession.setActionHandler('seekbackward', self.seekbackward)
                navigator.mediaSession.setActionHandler('seekforward', self.seekforward)
                navigator.mediaSession.setActionHandler('previoustrack', self.previoustrack)
                navigator.mediaSession.setActionHandler('nexttrack', self.nexttrack)
            def onended(event):
                return self.nexttrack()
            def onplay(event):
                self.toggle_button.checked = True
                if self.run_timer.checked:
                    self.start_timer()
            def onpause(event):
                self.toggle_button.checked = False
            self.audio.node.onended = onended
            self.audio.node.onplay = onplay
            self.audio.node.onpause = onpause
            self.title = "BeetMe"
            self.icon = "/beetme.png"
            setInterval(self.remember_current_time, 3000)

        def start_timer(self):
            self.end_time = moment().add(
                parseInt(self.time_min.text), "minutes",
                parseInt(self.time_sec.text), "seconds",
            )
            self.run_timer_interval = setInterval(self.up_timer, 1000)

        def remember_current_time(self):
            if not self.audio.node.paused:
                cookie.set("current_time", self.audio.node.currentTime)

        def play(self):
            self.audio.node.play()

        def pause(self):
            self.audio.node.pause()

        @event.connect("seekforward_button.mouse_click")
        def _seekforward(self, *evs):
            self.seekforward()

        def seekforward(self):
            self.audio.node.currentTime = Math.min(self.audio.node.currentTime + self.skipTime, self.audio.node.duration)

        @event.connect("seekbackward_button.mouse_click")
        def _seekbackward(self, *evs):
            self.seekbackward()

        def seekbackward(self, *evs):
            self.audio.node.currentTime = Math.max(self.audio.node.currentTime - self.skipTime, 0)

        @event.connect("prev_button.mouse_click")
        def _previoustrack(self, *evs):
            self.previoustrack()

        def previoustrack(self, *evs):
            self.select_prev()
            self._play_cache()

        def select_next(self):
            index_selected = self.cache_table.row({"selected": true}).index()
            indexes = self.cache_table.rows({"filter": "applied"}).indexes()
            maxvalue = indexes.length
            old_pos = indexes.indexOf(index_selected)
            new_index = indexes[((old_pos + 1) + maxvalue) % maxvalue]
            self.cache_table.row(new_index).select()

        def select_prev(self):
            index_selected = self.cache_table.row({"selected": true}).index()
            indexes = self.cache_table.rows({"filter": "applied"}).indexes()
            maxvalue = indexes.length
            old_pos = indexes.indexOf(index_selected)
            new_index = indexes[((old_pos - 1) + maxvalue) % maxvalue]
            self.cache_table.row(new_index).select()

        def select_rand(self):
            indexes = self.cache_table.rows({"filter": "applied"}).indexes()
            new_index = indexes[Math.floor(Math.random() * indexes.length)]
            self.cache_table.row(new_index).select()

        @event.connect("next_button.mouse_click")
        def _nexttrack(self, *evs):
            self.nexttrack()

        def nexttrack(self, *evs):
            if self.shuffle_button.checked:
                self.select_rand()
            else:
                self.select_next()
            self._play_cache()

        def select_near(self):
            index_selected = self.cache_table.row({"selected": true}).index()
            indexes = self.cache_table.rows({"filter": "applied"}).indexes()
            maxvalue = indexes.length
            old_pos = indexes.indexOf(index_selected)
            if old_pos == maxvalue - 1:
                self.select_prev()
            else:
                self.select_next()

        @event.connect("key_press")
        def _key_press(self, *evs):
            key = evs[-1].key
            if key == " ":
                self.toggle_button.checked = not self.toggle_button.checked

        @event.connect("key_down")
        def _key_down(self, *evs):
            key = evs[-1].key
            if key == 'ArrowRight':
                self.seekforward()
            elif key == 'ArrowLeft':
                self.seekbackward()
            elif key == "PageDown":
                self.nexttrack()
            elif key == "PageUp":
                self.previoustrack()

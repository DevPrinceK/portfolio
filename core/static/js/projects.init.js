var Shuffle = window.Shuffle;
class Demo {
    constructor(e) {
        this.element = e, this.shuffle = new Shuffle(e, {
            itemSelector: ".picture-item",
            sizer: e.querySelector(".my-sizer-element")
        }), this.addShuffleEventListeners(), this._activeFilters = [], this.addFilterButtons(), this.addSorting(), this.addSearchFilter()
    }
    addShuffleEventListeners() {
        this.shuffle.on(Shuffle.EventType.LAYOUT, e => {
            console.log("layout. data:", e)
        }), this.shuffle.on(Shuffle.EventType.REMOVED, e => {
            console.log("removed. data:", e)
        })
    }
    addFilterButtons() {
        const e = document.querySelector(".filter-options");
        if (!e) return;
        const t = Array.from(e.children),
            r = this._handleFilterClick.bind(this);
        t.forEach(e => {
            e.addEventListener("click", r, !1)
        })
    }
    _handleFilterClick(e) {
        const t = e.currentTarget,
            r = t.classList.contains("active"),
            i = t.getAttribute("data-group");
        let s;
        this._removeActiveClassFromChildren(t.parentNode), r ? (t.classList.remove("active"), s = Shuffle.ALL_ITEMS) : (t.classList.add("active"), s = i), this.shuffle.filter(s)
    }
    _removeActiveClassFromChildren(e) {
        const {
            children: t
        } = e;
        for (let e = t.length - 1; e >= 0; e--) t[e].classList.remove("active")
    }
    addSorting() {
        const e = document.querySelector(".sort-options");
        e && e.addEventListener("change", this._handleSortChange.bind(this))
    }
    _handleSortChange(e) {
        Array.from(e.currentTarget.children).forEach(t => {
            t.querySelector("input").value === e.target.value ? t.classList.add("active") : t.classList.remove("active")
        });
        const {
            value: t
        } = e.target;
        let r = {};
        "date-created" === t ? r = {
            reverse: !0,
            by: function(e) {
                return e.getAttribute("data-created")
            }
        } : "title" === t && (r = {
            by: function(e) {
                return e.getAttribute("data-title").toLowerCase()
            }
        }), this.shuffle.sort(r)
    }
    addSearchFilter() {
        const e = document.querySelector(".js-shuffle-search");
        e && e.addEventListener("keyup", this._handleSearchKeyup.bind(this))
    }
    _handleSearchKeyup(e) {
        const t = e.target.value.toLowerCase();
        this.shuffle.filter((e, r) => {
            if (r.group !== Shuffle.ALL_ITEMS) {
                if (!(-1 !== JSON.parse(e.getAttribute("data-groups")).indexOf(r.group))) return !1
            }
            return -1 !== e.querySelector(".picture-item__title").textContent.toLowerCase().trim().indexOf(t)
        })
    }
}
document.addEventListener("DOMContentLoaded", () => {
    window.demo = new Demo(document.getElementById("grid"))
});
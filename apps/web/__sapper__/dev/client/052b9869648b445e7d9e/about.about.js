(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["about"],{

/***/ "./src/routes/about.svelte":
/*!*********************************!*\
  !*** ./src/routes/about.svelte ***!
  \*********************************/
/*! exports provided: default, preload */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "preload", function() { return preload; });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var svelte_i18n__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte-i18n */ "./node_modules/svelte-i18n/dist/runtime.esm.js");
/* harmony import */ var _components_MarkDownPage__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../components/MarkDownPage */ "./src/components/MarkDownPage.svelte");
/* src/routes/about.svelte generated by Svelte v3.32.3 */




const file = "src/routes/about.svelte";

function create_fragment(ctx) {
	let markdownpage;
	let current;

	markdownpage = new _components_MarkDownPage__WEBPACK_IMPORTED_MODULE_2__["default"]({
			props: {
				readmeHTML: /*readmeHTML*/ ctx[0],
				title: "About LibreLingo",
				description: /*$_*/ ctx[1]("about.meta.description")
			},
			$$inline: true
		});

	const block = {
		c: function create() {
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["create_component"])(markdownpage.$$.fragment);
		},
		l: function claim(nodes) {
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["claim_component"])(markdownpage.$$.fragment, nodes);
		},
		m: function mount(target, anchor) {
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["mount_component"])(markdownpage, target, anchor);
			current = true;
		},
		p: function update(ctx, [dirty]) {
			const markdownpage_changes = {};
			if (dirty & /*readmeHTML*/ 1) markdownpage_changes.readmeHTML = /*readmeHTML*/ ctx[0];
			if (dirty & /*$_*/ 2) markdownpage_changes.description = /*$_*/ ctx[1]("about.meta.description");
			markdownpage.$set(markdownpage_changes);
		},
		i: function intro(local) {
			if (current) return;
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["transition_in"])(markdownpage.$$.fragment, local);
			current = true;
		},
		o: function outro(local) {
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["transition_out"])(markdownpage.$$.fragment, local);
			current = false;
		},
		d: function destroy(detaching) {
			Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["destroy_component"])(markdownpage, detaching);
		}
	};

	Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["dispatch_dev"])("SvelteRegisterBlock", {
		block,
		id: create_fragment.name,
		type: "component",
		source: "",
		ctx
	});

	return block;
}

async function preload() {
	return {
		readmeHTML: (await Object(_components_MarkDownPage__WEBPACK_IMPORTED_MODULE_2__["getMarkDownData"])(await __webpack_require__.e(/*! import() */ 34).then(__webpack_require__.bind(null, /*! ../../../../README.md */ "../../README.md")))).contents.split("<h2>Tech stack</h2>")[0]
	};
}

function instance($$self, $$props, $$invalidate) {
	let $_;
	Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["validate_store"])(svelte_i18n__WEBPACK_IMPORTED_MODULE_1__["_"], "_");
	Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["component_subscribe"])($$self, svelte_i18n__WEBPACK_IMPORTED_MODULE_1__["_"], $$value => $$invalidate(1, $_ = $$value));
	let { $$slots: slots = {}, $$scope } = $$props;
	Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["validate_slots"])("About", slots, []);
	let { readmeHTML } = $$props;
	const writable_props = ["readmeHTML"];

	Object.keys($$props).forEach(key => {
		if (!~writable_props.indexOf(key) && key.slice(0, 2) !== "$$") console.warn(`<About> was created with unknown prop '${key}'`);
	});

	$$self.$$set = $$props => {
		if ("readmeHTML" in $$props) $$invalidate(0, readmeHTML = $$props.readmeHTML);
	};

	$$self.$capture_state = () => ({
		MarkDownPage: _components_MarkDownPage__WEBPACK_IMPORTED_MODULE_2__["default"],
		getMarkDownData: _components_MarkDownPage__WEBPACK_IMPORTED_MODULE_2__["getMarkDownData"],
		_: svelte_i18n__WEBPACK_IMPORTED_MODULE_1__["_"],
		preload,
		readmeHTML,
		$_
	});

	$$self.$inject_state = $$props => {
		if ("readmeHTML" in $$props) $$invalidate(0, readmeHTML = $$props.readmeHTML);
	};

	if ($$props && "$$inject" in $$props) {
		$$self.$inject_state($$props.$$inject);
	}

	return [readmeHTML, $_];
}

class About extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__["SvelteComponentDev"] {
	constructor(options) {
		super(options);
		Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["init"])(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__["safe_not_equal"], { readmeHTML: 0 });

		Object(svelte_internal__WEBPACK_IMPORTED_MODULE_0__["dispatch_dev"])("SvelteRegisterComponent", {
			component: this,
			tagName: "About",
			options,
			id: create_fragment.name
		});

		const { ctx } = this.$$;
		const props = options.props || {};

		if (/*readmeHTML*/ ctx[0] === undefined && !("readmeHTML" in props)) {
			console.warn("<About> was created without expected prop 'readmeHTML'");
		}
	}

	get readmeHTML() {
		throw new Error("<About>: Props cannot be read directly from the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}

	set readmeHTML(value) {
		throw new Error("<About>: Props cannot be set directly on the component instance unless compiling with 'accessors: true' or '<svelte:options accessors/>'");
	}
}

/* harmony default export */ __webpack_exports__["default"] = (About);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zcmMvcm91dGVzL2Fib3V0LnN2ZWx0ZSJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFDZ0M7QUFEc0Y7Ozs7Ozs7OzsrQkFhdkcsR0FBVTs7d0JBRVQsR0FBRSxJQUFDLHdCQUF3Qjs7Ozs7Ozs7Ozs7Ozs7Ozs7O2tGQUY1QixHQUFVO21FQUVULEdBQUUsSUFBQyx3QkFBd0I7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7ZUFickIsT0FBTzs7RUFFckIsVUFBVSxTQUFTLGdGQUFlLE9BQU8sOEhBQStCLEdBQUcsUUFBUSxDQUFDLEtBQUssQ0FBQyxxQkFBcUIsRUFBRSxDQUFDOzs7Ozs7Ozs7O09BS3JGLFVBQVUiLCJmaWxlIjoiMDUyYjk4Njk2NDhiNDQ1ZTdkOWUvYWJvdXQuYWJvdXQuanMiLCJzb3VyY2VzQ29udGVudCI6WyI8c2NyaXB0IGxhbmc9XCJ0eXBlc2NyaXB0XCIgY29udGV4dD1cIm1vZHVsZVwiPmltcG9ydCBNYXJrRG93blBhZ2UsIHsgZ2V0TWFya0Rvd25EYXRhIH0gZnJvbSBcIi4uL2NvbXBvbmVudHMvTWFya0Rvd25QYWdlXCI7XG5pbXBvcnQgeyBfIH0gZnJvbSBcInN2ZWx0ZS1pMThuXCI7XG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gcHJlbG9hZCgpIHtcbiAgICByZXR1cm4ge1xuICAgICAgICByZWFkbWVIVE1MOiAoYXdhaXQgZ2V0TWFya0Rvd25EYXRhKGF3YWl0IGltcG9ydChcIi4uLy4uLy4uLy4uL1JFQURNRS5tZFwiKSkpLmNvbnRlbnRzLnNwbGl0KFwiPGgyPlRlY2ggc3RhY2s8L2gyPlwiKVswXSxcbiAgICB9O1xufVxuPC9zY3JpcHQ+XG5cbjxzY3JpcHQgbGFuZz1cInR5cGVzY3JpcHRcIj5leHBvcnQgbGV0IHJlYWRtZUhUTUw7XG48L3NjcmlwdD5cblxuPE1hcmtEb3duUGFnZVxuICByZWFkbWVIVE1MPVwie3JlYWRtZUhUTUx9XCJcbiAgdGl0bGU9XCJBYm91dCBMaWJyZUxpbmdvXCJcbiAgZGVzY3JpcHRpb249XCJ7JF8oJ2Fib3V0Lm1ldGEuZGVzY3JpcHRpb24nKX1cIiAvPlxuIl0sInNvdXJjZVJvb3QiOiIifQ==
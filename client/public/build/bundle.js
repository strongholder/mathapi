var app=function(){"use strict";function t(){}function n(t){return t()}function e(){return Object.create(null)}function o(t){t.forEach(n)}function r(t){return"function"==typeof t}function u(t,n){return t!=t?n==n:t!==n||t&&"object"==typeof t||"function"==typeof t}function l(t,n){t.appendChild(n)}function i(t,n,e){t.insertBefore(n,e||null)}function c(t){t.parentNode.removeChild(t)}function s(t){return document.createElement(t)}function a(t){return document.createTextNode(t)}function f(){return a(" ")}function d(t,n,e,o){return t.addEventListener(n,e,o),()=>t.removeEventListener(n,e,o)}function p(t,n,e){null==e?t.removeAttribute(n):t.getAttribute(n)!==e&&t.setAttribute(n,e)}function $(t){return""===t?null:+t}function m(t,n){n=""+n,t.wholeText!==n&&(t.data=n)}function h(t,n){t.value=null==n?"":n}let g;function v(t){g=t}function b(){const t=function(){if(!g)throw new Error("Function called outside component initialization");return g}();return(n,e)=>{const o=t.$$.callbacks[n];if(o){const r=function(t,n){const e=document.createEvent("CustomEvent");return e.initCustomEvent(t,!1,!1,n),e}(n,e);o.slice().forEach((n=>{n.call(t,r)}))}}}const y=[],x=[],k=[],w=[],C=Promise.resolve();let _=!1;function j(t){k.push(t)}function O(t){w.push(t)}let E=!1;const S=new Set;function M(){if(!E){E=!0;do{for(let t=0;t<y.length;t+=1){const n=y[t];v(n),N(n.$$)}for(v(null),y.length=0;x.length;)x.pop()();for(let t=0;t<k.length;t+=1){const n=k[t];S.has(n)||(S.add(n),n())}k.length=0}while(y.length);for(;w.length;)w.pop()();_=!1,E=!1,S.clear()}}function N(t){if(null!==t.fragment){t.update(),o(t.before_update);const n=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,n),t.after_update.forEach(j)}}const T=new Set;function A(t,n){t&&t.i&&(T.delete(t),t.i(n))}function J(t,n,e,o){if(t&&t.o){if(T.has(t))return;T.add(t),undefined.c.push((()=>{T.delete(t),o&&(e&&t.d(1),o())})),t.o(n)}}function P(t,n){t.d(1),n.delete(t.key)}function q(t,n,e){const o=t.$$.props[n];void 0!==o&&(t.$$.bound[o]=e,e(t.$$.ctx[o]))}function L(t){t&&t.c()}function z(t,e,u){const{fragment:l,on_mount:i,on_destroy:c,after_update:s}=t.$$;l&&l.m(e,u),j((()=>{const e=i.map(n).filter(r);c?c.push(...e):o(e),t.$$.on_mount=[]})),s.forEach(j)}function B(t,n){const e=t.$$;null!==e.fragment&&(o(e.on_destroy),e.fragment&&e.fragment.d(n),e.on_destroy=e.fragment=null,e.ctx=[])}function F(t,n){-1===t.$$.dirty[0]&&(y.push(t),_||(_=!0,C.then(M)),t.$$.dirty.fill(0)),t.$$.dirty[n/31|0]|=1<<n%31}function W(n,r,u,l,i,s,a=[-1]){const f=g;v(n);const d=r.props||{},p=n.$$={fragment:null,ctx:null,props:s,update:t,not_equal:i,bound:e(),on_mount:[],on_destroy:[],before_update:[],after_update:[],context:new Map(f?f.$$.context:[]),callbacks:e(),dirty:a,skip_bound:!1};let $=!1;if(p.ctx=u?u(n,d,((t,e,...o)=>{const r=o.length?o[0]:e;return p.ctx&&i(p.ctx[t],p.ctx[t]=r)&&(!p.skip_bound&&p.bound[t]&&p.bound[t](r),$&&F(n,t)),e})):[],p.update(),$=!0,o(p.before_update),p.fragment=!!l&&l(p.ctx),r.target){if(r.hydrate){const t=function(t){return Array.from(t.childNodes)}(r.target);p.fragment&&p.fragment.l(t),t.forEach(c)}else p.fragment&&p.fragment.c();r.intro&&A(n.$$.fragment),z(n,r.target,r.anchor),M()}v(f)}class D{$destroy(){B(this,1),this.$destroy=t}$on(t,n){const e=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return e.push(n),()=>{const t=e.indexOf(n);-1!==t&&e.splice(t,1)}}$set(t){var n;this.$$set&&(n=t,0!==Object.keys(n).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}function G(t){let n,e,r,u,g,v,b,y,x,k,w,C,_,j,O,E;return{c(){n=s("h1"),n.textContent="Compute the power:",e=f(),r=s("input"),u=f(),g=s("input"),v=f(),b=s("button"),b.textContent="Compute",y=f(),x=s("h3"),k=a(t[2]),w=s("sup"),C=a(t[3]),_=a(" = "),j=a(t[0]),p(r,"type","number"),p(r,"name","base"),p(r,"placeholder","base"),p(r,"step","1"),p(g,"type","number"),p(g,"name","base"),p(g,"placeholder","exponent"),p(g,"step","1")},m(o,c){i(o,n,c),i(o,e,c),i(o,r,c),h(r,t[2]),i(o,u,c),i(o,g,c),h(g,t[3]),i(o,v,c),i(o,b,c),i(o,y,c),i(o,x,c),l(x,k),l(x,w),l(w,C),l(x,_),l(x,j),O||(E=[d(r,"input",t[5]),d(g,"input",t[6]),d(b,"click",t[4])],O=!0)},p(t,n){4&n&&$(r.value)!==t[2]&&h(r,t[2]),8&n&&$(g.value)!==t[3]&&h(g,t[3]),4&n&&m(k,t[2]),8&n&&m(C,t[3]),1&n&&m(j,t[0])},d(t){t&&c(n),t&&c(e),t&&c(r),t&&c(u),t&&c(g),t&&c(v),t&&c(b),t&&c(y),t&&c(x),O=!1,o(E)}}}function H(n){let e;return{c(){e=s("div"),e.textContent="loading...",p(e,"class","loading svelte-1j5ordv")},m(t,n){i(t,e,n)},p:t,d(t){t&&c(e)}}}function I(n){let e;function o(t,n){return t[1]?H:G}let r=o(n),u=r(n);return{c(){e=s("div"),u.c(),p(e,"class","main svelte-1j5ordv")},m(t,n){i(t,e,n),u.m(e,null)},p(t,[n]){r===(r=o(t))&&u?u.p(t,n):(u.d(1),u=r(t),u&&(u.c(),u.m(e,null)))},i:t,o:t,d(t){t&&c(e),u.d()}}}function K(t,n,e){let{result:o="?"}=n,{loading:r=!1}=n;const u=b();let l=0,i=1;return t.$$set=t=>{"result"in t&&e(0,o=t.result),"loading"in t&&e(1,r=t.loading)},t.$$.update=()=>{12&t.$$.dirty&&e(0,o="?")},[o,r,l,i,function(){e(2,l=Math.floor(l)),e(3,i=Math.floor(i)),u("value",{base:l,exponent:i})},function(){l=$(this.value),e(2,l)},function(){i=$(this.value),e(3,i)}]}class Q extends D{constructor(t){super(),W(this,t,K,I,u,{result:0,loading:1})}}function R(t){let n,e,r,u,g,v,b,y,x,k,w,C,_;return{c(){n=s("h1"),n.textContent="Compute nth fibonacci number:",e=f(),r=s("input"),u=f(),g=s("button"),g.textContent="Compute",v=f(),b=s("h3"),y=a("fib("),x=a(t[2]),k=a(") = "),w=a(t[0]),p(r,"type","number"),p(r,"name","number"),p(r,"placeholder","number"),p(r,"step","1")},m(o,c){i(o,n,c),i(o,e,c),i(o,r,c),h(r,t[2]),i(o,u,c),i(o,g,c),i(o,v,c),i(o,b,c),l(b,y),l(b,x),l(b,k),l(b,w),C||(_=[d(r,"input",t[4]),d(g,"click",t[3])],C=!0)},p(t,n){4&n&&$(r.value)!==t[2]&&h(r,t[2]),4&n&&m(x,t[2]),1&n&&m(w,t[0])},d(t){t&&c(n),t&&c(e),t&&c(r),t&&c(u),t&&c(g),t&&c(v),t&&c(b),C=!1,o(_)}}}function U(n){let e;return{c(){e=s("div"),e.textContent="loading...",p(e,"class","loading svelte-1j5ordv")},m(t,n){i(t,e,n)},p:t,d(t){t&&c(e)}}}function V(n){let e;function o(t,n){return t[1]?U:R}let r=o(n),u=r(n);return{c(){e=s("div"),u.c(),p(e,"class","main svelte-1j5ordv")},m(t,n){i(t,e,n),u.m(e,null)},p(t,[n]){r===(r=o(t))&&u?u.p(t,n):(u.d(1),u=r(t),u&&(u.c(),u.m(e,null)))},i:t,o:t,d(t){t&&c(e),u.d()}}}function X(t,n,e){let{result:o="?"}=n,{loading:r=!1}=n;const u=b();let l=0;return t.$$set=t=>{"result"in t&&e(0,o=t.result),"loading"in t&&e(1,r=t.loading)},t.$$.update=()=>{4&t.$$.dirty&&e(0,o="?")},[o,r,l,function(){e(2,l=Math.floor(l)),u("value",{number:l})},function(){l=$(this.value),e(2,l)}]}class Y extends D{constructor(t){super(),W(this,t,X,V,u,{result:0,loading:1})}}function Z(t){let n,e,r,u,g,v,b,y,x,k,w,C;return{c(){n=s("h1"),n.textContent="Compute n!:",e=f(),r=s("input"),u=f(),g=s("button"),g.textContent="Compute",v=f(),b=s("h3"),y=a(t[2]),x=a("! = "),k=a(t[0]),p(r,"type","number"),p(r,"name","number"),p(r,"placeholder","number"),p(r,"step","1")},m(o,c){i(o,n,c),i(o,e,c),i(o,r,c),h(r,t[2]),i(o,u,c),i(o,g,c),i(o,v,c),i(o,b,c),l(b,y),l(b,x),l(b,k),w||(C=[d(r,"input",t[4]),d(g,"click",t[3])],w=!0)},p(t,n){4&n&&$(r.value)!==t[2]&&h(r,t[2]),4&n&&m(y,t[2]),1&n&&m(k,t[0])},d(t){t&&c(n),t&&c(e),t&&c(r),t&&c(u),t&&c(g),t&&c(v),t&&c(b),w=!1,o(C)}}}function tt(n){let e;return{c(){e=s("div"),e.textContent="loading...",p(e,"class","loading svelte-1j5ordv")},m(t,n){i(t,e,n)},p:t,d(t){t&&c(e)}}}function nt(n){let e;function o(t,n){return t[1]?tt:Z}let r=o(n),u=r(n);return{c(){e=s("div"),u.c(),p(e,"class","main svelte-1j5ordv")},m(t,n){i(t,e,n),u.m(e,null)},p(t,[n]){r===(r=o(t))&&u?u.p(t,n):(u.d(1),u=r(t),u&&(u.c(),u.m(e,null)))},i:t,o:t,d(t){t&&c(e),u.d()}}}function et(t,n,e){let{result:o="?"}=n,{loading:r=!1}=n;const u=b();let l=0;return t.$$set=t=>{"result"in t&&e(0,o=t.result),"loading"in t&&e(1,r=t.loading)},t.$$.update=()=>{4&t.$$.dirty&&e(0,o="?")},[o,r,l,function(){e(2,l=Math.floor(l)),u("value",{number:l})},function(){l=$(this.value),e(2,l)}]}class ot extends D{constructor(t){super(),W(this,t,et,nt,u,{result:0,loading:1})}}function rt(t,n,e){const o=t.slice();return o[1]=n[e][0],o[2]=n[e][1],o}function ut(t){let n,e=[],o=new Map,r=Object.entries(t[0]);const u=t=>t[1];for(let n=0;n<r.length;n+=1){let l=rt(t,r,n),i=u(l);o.set(i,e[n]=lt(i,l))}return{c(){n=s("ul");for(let t=0;t<e.length;t+=1)e[t].c();p(n,"class","svelte-1qlk277")},m(t,o){i(t,n,o);for(let t=0;t<e.length;t+=1)e[t].m(n,null)},p(t,l){1&l&&(r=Object.entries(t[0]),e=function(t,n,e,o,r,u,l,i,c,s,a,f){let d=t.length,p=u.length,$=d;const m={};for(;$--;)m[t[$].key]=$;const h=[],g=new Map,v=new Map;for($=p;$--;){const t=f(r,u,$),i=e(t);let c=l.get(i);c?o&&c.p(t,n):(c=s(i,t),c.c()),g.set(i,h[$]=c),i in m&&v.set(i,Math.abs($-m[i]))}const b=new Set,y=new Set;function x(t){A(t,1),t.m(i,a),l.set(t.key,t),a=t.first,p--}for(;d&&p;){const n=h[p-1],e=t[d-1],o=n.key,r=e.key;n===e?(a=n.first,d--,p--):g.has(r)?!l.has(o)||b.has(o)?x(n):y.has(r)?d--:v.get(o)>v.get(r)?(y.add(o),x(n)):(b.add(r),d--):(c(e,l),d--)}for(;d--;){const n=t[d];g.has(n.key)||c(n,l)}for(;p;)x(h[p-1]);return h}(e,l,u,1,t,r,o,n,P,lt,null,rt))},d(t){t&&c(n);for(let t=0;t<e.length;t+=1)e[t].d()}}}function lt(t,n){let e,o,r,u,f,d=n[1]+"",p=n[2]+"";return{key:t,first:null,c(){e=s("li"),o=s("strong"),r=a(d),u=a(": "),f=a(p),this.first=e},m(t,n){i(t,e,n),l(e,o),l(o,r),l(o,u),l(e,f)},p(t,e){n=t,1&e&&d!==(d=n[1]+"")&&m(r,d),1&e&&p!==(p=n[2]+"")&&m(f,p)},d(t){t&&c(e)}}}function it(n){let e,o=Object.entries(n[0]).length>0,r=o&&ut(n);return{c(){r&&r.c(),e=a("")},m(t,n){r&&r.m(t,n),i(t,e,n)},p(t,[n]){1&n&&(o=Object.entries(t[0]).length>0),o?r?r.p(t,n):(r=ut(t),r.c(),r.m(e.parentNode,e)):r&&(r.d(1),r=null)},i:t,o:t,d(t){r&&r.d(t),t&&c(e)}}}function ct(t,n,e){let{errors:o={}}=n;return t.$$set=t=>{"errors"in t&&e(0,o=t.errors)},[o]}class st extends D{constructor(t){super(),W(this,t,ct,it,u,{errors:0})}}function at(t){let n,e,o,r,u,a,d,$,m,h,g,v,b,y,k,w,C,_;function j(n){t[11].call(null,n)}let E={};function S(n){t[12].call(null,n)}function M(n){t[13].call(null,n)}void 0!==t[6]&&(E.errors=t[6]),r=new st({props:E}),x.push((()=>q(r,"errors",j)));let N={};function T(n){t[14].call(null,n)}function P(n){t[15].call(null,n)}void 0!==t[0]&&(N.result=t[0]),void 0!==t[3]&&(N.loading=t[3]),d=new Q({props:N}),x.push((()=>q(d,"result",S))),x.push((()=>q(d,"loading",M))),d.$on("value",t[7]);let F={};function W(n){t[16].call(null,n)}function D(n){t[17].call(null,n)}void 0!==t[1]&&(F.result=t[1]),void 0!==t[4]&&(F.loading=t[4]),g=new Y({props:F}),x.push((()=>q(g,"result",T))),x.push((()=>q(g,"loading",P))),g.$on("value",t[8]);let G={};return void 0!==t[2]&&(G.result=t[2]),void 0!==t[5]&&(G.loading=t[5]),k=new ot({props:G}),x.push((()=>q(k,"result",W))),x.push((()=>q(k,"loading",D))),k.$on("value",t[9]),{c(){n=s("main"),e=s("h1"),e.textContent="Welcome to Mathapi!",o=f(),L(r.$$.fragment),a=f(),L(d.$$.fragment),h=f(),L(g.$$.fragment),y=f(),L(k.$$.fragment),p(e,"class","svelte-1tky8bj"),p(n,"class","svelte-1tky8bj")},m(t,u){i(t,n,u),l(n,e),l(n,o),z(r,n,null),l(n,a),z(d,n,null),l(n,h),z(g,n,null),l(n,y),z(k,n,null),_=!0},p(t,[n]){const e={};!u&&64&n&&(u=!0,e.errors=t[6],O((()=>u=!1))),r.$set(e);const o={};!$&&1&n&&($=!0,o.result=t[0],O((()=>$=!1))),!m&&8&n&&(m=!0,o.loading=t[3],O((()=>m=!1))),d.$set(o);const l={};!v&&2&n&&(v=!0,l.result=t[1],O((()=>v=!1))),!b&&16&n&&(b=!0,l.loading=t[4],O((()=>b=!1))),g.$set(l);const i={};!w&&4&n&&(w=!0,i.result=t[2],O((()=>w=!1))),!C&&32&n&&(C=!0,i.loading=t[5],O((()=>C=!1))),k.$set(i)},i(t){_||(A(r.$$.fragment,t),A(d.$$.fragment,t),A(g.$$.fragment,t),A(k.$$.fragment,t),_=!0)},o(t){J(r.$$.fragment,t),J(d.$$.fragment,t),J(g.$$.fragment,t),J(k.$$.fragment,t),_=!1},d(t){t&&c(n),B(r),B(d),B(g),B(k)}}}function ft(t){return JSON.parse(t.replace(/(?<!")(\b\d+\b)(?!")/g,'"$1"'))}function dt(t,n,e){let{api_uri:o}=n;const r=`${o}/exponent`,u=`${o}/fibonacci`,l=`${o}/factorial`;let i,c,s,a,f,d,p={};return t.$$set=t=>{"api_uri"in t&&e(10,o=t.api_uri)},[i,c,s,a,f,d,p,async function(t){e(3,a=!0);const n=await fetch(r,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(t.detail)}),o=ft(await n.text());e(3,a=!1),n.ok?(e(6,p={}),e(0,i=o.result)):e(6,p=o.message)},async function(t){e(4,f=!0);const n=await fetch(u,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(t.detail)}),o=ft(await n.text());e(4,f=!1),n.ok?(e(6,p={}),e(1,c=o.result)):e(6,p=o.message)},async function(t){e(5,d=!0);const n=await fetch(l,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(t.detail)}),o=ft(await n.text());e(5,d=!1),n.ok?(e(6,p={}),e(2,s=o.result)):e(6,p=o.message)},o,function(t){p=t,e(6,p)},function(t){i=t,e(0,i)},function(t){a=t,e(3,a)},function(t){c=t,e(1,c)},function(t){f=t,e(4,f)},function(t){s=t,e(2,s)},function(t){d=t,e(5,d)}]}return new class extends D{constructor(t){super(),W(this,t,dt,at,u,{api_uri:10})}}({target:document.body,props:{api_uri:"/api/v1"}})}();
//# sourceMappingURL=bundle.js.map

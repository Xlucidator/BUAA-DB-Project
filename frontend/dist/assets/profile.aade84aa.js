import{d as w,v as B,b as a,e as D,g as l,w as d,f as e,y as c,i,F as I,Z as S,a as s,p as A,m as V,h as F,o as L,k as P,_ as z}from"./index.620621f6.js";const o=_=>(A("data-v-3c1664ce"),_=_(),V(),_),E={class:"block"},T=o(()=>e("br",null,null,-1)),U={class:"text-3xl",style:{color:"#333333"}},Z=o(()=>e("span",{class:"information text-xl lineHeight"},"Class: ",-1)),j={class:"data text-xl lineHeight"},q=o(()=>e("br",null,null,-1)),G=o(()=>e("span",{class:"information text-xl lineHeight"},"Region: ",-1)),J={class:"data text-xl lineHeight"},K=o(()=>e("br",null,null,-1)),M=o(()=>e("span",{class:"information text-xl lineHeight"},"Race: ",-1)),O={class:"data text-xl lineHeight"},Q=o(()=>e("br",null,null,-1)),W=o(()=>e("span",{class:"information text-xl lineHeight"},"Description: ",-1)),X={class:"data text-xl lineHeight"},Y=w({__name:"profile",setup(_){const r=B.state.user.CodeName;let x=a(""),m=r,u=a(""),p=a(""),f=a(""),h=a("");const v=F();function C(n){console.log("index/profile/"+n+"/"),S.get("index/profile/"+n+"/").then(t=>{if(console.log(t),t.status!==200)return console.log("failed to get"),"";console.log("loadProfile",t.data),x.value=t.data.Avatar,u.value=t.data.Class,p.value=t.data.Region,f.value=t.data.Race,h.value=t.data.Description}).catch(t=>(console.log("axios failed"),console.log(t),"")),console.log("index/profile/"+n+"/")}const b=()=>{v.go(-1)};return C(r),(n,t)=>{const H=s("ArrowLeft"),g=s("el-icon"),k=s("el-button"),R=s("el-avatar"),y=s("star-filled"),N=s("el-divider");return L(),D(I,null,[l(k,{onClick:b,style:{"margin-top":"3%","margin-left":"5%"}},{default:d(()=>[l(g,null,{default:d(()=>[l(H)]),_:1}),P(" back ")]),_:1}),e("div",E,[l(R,{size:150,src:n.circleUrl},null,8,["src"]),T,e("p",U,c(i(m)),1),l(N,null,{default:d(()=>[l(g,null,{default:d(()=>[l(y)]),_:1})]),_:1})]),e("div",null,[Z,e("span",j,c(i(u)),1),q,G,e("span",J,c(i(p)),1),K,M,e("span",O,c(i(f)),1),Q,W,e("span",X,c(i(h)),1)])],64)}}});const ee=z(Y,[["__scopeId","data-v-3c1664ce"]]);export{ee as default};

import{_ as D,b as m,r as L,e as z,f as d,g as l,w as t,i as a,F as _,h as A,q as F,a as u,o as c,t as b,c as V,k as C,p as K,m as $}from"./index.620621f6.js";import{N as r}from"./utils.f640e782.js";const y=g=>(K("data-v-2ce42905"),g=g(),$(),g),T=y(()=>d("div",{class:"register"},[d("span",{class:"text-5xl"}," -- REGISTER -- ")],-1)),E={class:"input-box"},O={class:"test-box"},j={class:"Button"},G={class:"jump"},M=y(()=>d("p",{style:{color:"#888888"}},"yes i already have an account",-1)),q={__name:"register",setup(g){const w=A();let p=m(1);const o=L({CodeName:"",Password:"",PwConfirm:"",Class:"",Region:"",Race:"",Description:""}),x=()=>{w.push("/login")},k=s=>{s!==""?/^[A-za-z0-9][A-za-z0-9'.\s]*$/.test(s)?p.value=1:(r(0,"contains only alnum and . and space"),p.value=0):(p.value=0,r(0,"CodeName shouldn't be null"))},S=()=>{o.Password===""&&r(0,"passwords not null"),o.Password!==o.PwConfirm?r(0,"passwords do not coordinate"):p.value?F(o).then(s=>{console.log(s),s.status!==200&&s.status!==201?"details"in s.data?r(0,s.data.details):r(0,"ops~! other error"):(r(1,"registered successfully"),w.push("/login"))}).catch(s=>{console.log(s),r(0,s.msg)}):r(0,"please check your CodeName")},N=m([{zhcn:"\u8FD1\u536B\u5E72\u5458",eng:"Guard"},{zhcn:"\u72D9\u51FB\u5E72\u5458",eng:"Sniper"},{zhcn:"\u91CD\u88C5\u5E72\u5458",eng:"Defender"},{zhcn:"\u533B\u7597\u5E72\u5458",eng:"Medic"},{zhcn:"\u8F85\u52A9\u5E72\u5458",eng:"Supporter"},{zhcn:"\u672F\u5E08\u5E72\u5458",eng:"Caster"},{zhcn:"\u7279\u79CD\u5E72\u5458",eng:"Specialist"},{zhcn:"\u5148\u950B\u5E72\u5458",eng:"Vanguard"}]),R=m([{zhcn:"\u708E",eng:"Yan"},{zhcn:"\u54E5\u4F26\u6BD4\u4E9A",eng:"Columbia"},{zhcn:"\u5361\u897F\u7C73\u5C14",eng:"Kazimierz"},{zhcn:"\u8C22\u62C9\u683C",eng:"Kjerag"},{zhcn:"\u62C9\u7279\u5170",eng:"Laterano"},{zhcn:"\u83B1\u5854\u5C3C\u4E9A",eng:"Leithanien"},{zhcn:"\u96F7\u59C6\u5FC5\u62D3",eng:"Rim Billiton"},{zhcn:"\u8428\u7C73",eng:"Sami"},{zhcn:"\u7C73\u8BFA\u65AF",eng:"Minos"},{zhcn:"\u73BB\u5229\u74E6\u5C14",eng:"Bol\xEDvar"},{zhcn:"\u8428\u5C14\u8D21",eng:"Sargon"},{zhcn:"\u53D9\u62C9\u53E4",eng:"Siracusa"},{zhcn:"\u7EF4\u591A\u5229\u4E9A",eng:"Victoria"},{zhcn:"\u5361\u5179\u6234\u5C14",eng:"Kazdel"},{zhcn:"\u4F0A\u6BD4\u5229\u4E9A",eng:"Iberia"},{zhcn:"\u963F\u6208\u5C14",eng:"\xC6gir"},{zhcn:"\u7F57\u5FB7\u5C9B",eng:"Rhodes Island"},{zhcn:"\u672A\u77E5",eng:"Unknown"}]),P=m([{zhcn:"\u9F99",eng:"Lung"},{zhcn:"\u9ECE\u535A\u5229",eng:"Liberi"},{zhcn:"\u9C81\u73C0",eng:"Lupo"},{zhcn:"\u9B3C",eng:"Oni"},{zhcn:"\u963F\u8FBE\u514B\u5229\u65AF",eng:"Archosauria"},{zhcn:"\u8428\u79D1\u5854",eng:"Sankta"},{zhcn:"\u8428\u5361\u5179",eng:"Sarkaz"},{zhcn:"\u83F2\u6797",eng:"Feline"},{zhcn:"\u74E6\u4F0A\u51E1",eng:"Vouivre"},{zhcn:"\u5FB7\u62C9\u514B",eng:"Draco"},{zhcn:"\u6C83\u5C14\u73C0",eng:"Vulpo"},{zhcn:"\u675C\u6797",eng:"Durin"},{zhcn:"\u672D\u62C9\u514B",eng:"Zalak"},{zhcn:"\u5E93\u5170\u5854",eng:"Kuranta"},{zhcn:"\u5361\u7279\u65AF",eng:"Cautus"},{zhcn:"\u5361\u666E\u91CC\u5C3C",eng:"Caprinae"},{zhcn:"\u4F69\u6D1B",eng:"Perro"},{zhcn:"\u4E30\u8E44",eng:"Forte"},{zhcn:"\u4E4C\u8428\u65AF",eng:"Ursus"},{zhcn:"\u963F\u65AF\u5170",eng:"Aslan"},{zhcn:"\u9E92\u9E9F",eng:"Kylin"},{zhcn:"\u963F\u6208\u5C14",eng:"\xC6gir"},{zhcn:"\u672A\u77E5",eng:"Unknown"}]);return(s,n)=>{const h=u("el-input"),i=u("el-form-item"),f=u("el-option"),v=u("el-select"),B=u("el-form"),U=u("Button"),I=u("el-button");return c(),z(_,null,[T,d("div",E,[l(B,{model:a(o),"label-width":"120px"},{default:t(()=>[l(i,{label:"CodeName"},{default:t(()=>[l(h,{modelValue:a(o).CodeName,"onUpdate:modelValue":n[0]||(n[0]=e=>a(o).CodeName=e),onBlur:n[1]||(n[1]=e=>k(a(o).CodeName))},null,8,["modelValue"])]),_:1}),l(i,{label:"Password"},{default:t(()=>[l(h,{modelValue:a(o).Password,"onUpdate:modelValue":n[2]||(n[2]=e=>a(o).Password=e),"show-password":!0},null,8,["modelValue"])]),_:1}),l(i,{label:"Password again"},{default:t(()=>[l(h,{modelValue:a(o).PwConfirm,"onUpdate:modelValue":n[3]||(n[3]=e=>a(o).PwConfirm=e),"show-password":!0},null,8,["modelValue"])]),_:1}),l(i,{label:"Class"},{default:t(()=>[l(v,{modelValue:a(o).Class,"onUpdate:modelValue":n[4]||(n[4]=e=>a(o).Class=e),placeholder:"please select your class"},{default:t(()=>[(c(!0),z(_,null,b(N.value,e=>(c(),V(f,{label:e.zhcn,value:e.eng},null,8,["label","value"]))),256))]),_:1},8,["modelValue"])]),_:1}),l(i,{label:"Region"},{default:t(()=>[l(v,{modelValue:a(o).Region,"onUpdate:modelValue":n[5]||(n[5]=e=>a(o).Region=e),placeholder:"please select your zone"},{default:t(()=>[(c(!0),z(_,null,b(R.value,e=>(c(),V(f,{label:e.zhcn,value:e.eng},null,8,["label","value"]))),256))]),_:1},8,["modelValue"])]),_:1}),l(i,{label:"Race"},{default:t(()=>[l(v,{modelValue:a(o).Race,"onUpdate:modelValue":n[6]||(n[6]=e=>a(o).Race=e),placeholder:"please select your zone"},{default:t(()=>[(c(!0),z(_,null,b(P.value,e=>(c(),V(f,{label:e.zhcn,value:e.eng},null,8,["label","value"]))),256))]),_:1},8,["modelValue"])]),_:1}),l(i,{label:"Description"},{default:t(()=>[d("div",O,[l(h,{modelValue:a(o).Description,"onUpdate:modelValue":n[7]||(n[7]=e=>a(o).Description=e),type:"textarea",autosize:""},null,8,["modelValue"])])]),_:1})]),_:1},8,["model"])]),d("div",j,[l(U,{tabindex:"-1",class:"transition !duration-300 focus:outline-none w-full py-3 rounded font-bold text-white bg-blue-400 ring-4 ring-blue-500 ring-opacity-50 cursor-pointer hover:bg-indigo-400 hover:ring-indigo-500 transform hover:scale-110 hover:-translate-y-1 hover:shadow-xl hover:opacity-80 shadow-indigo-500",onClick:n[8]||(n[8]=e=>S())},{default:t(()=>[C(" register ")]),_:1})]),d("div",G,[M,l(I,{tabindex:"-1",onClick:n[9]||(n[9]=e=>x())},{default:t(()=>[C(" click me to log in ")]),_:1})])],64)}}},H=D(q,[["__scopeId","data-v-2ce42905"]]);export{H as default};
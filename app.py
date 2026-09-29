import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="36 Presents — Digital Sphere",
    page_icon="36",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], .stApp {
    background:#01060b !important;
}
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding:0 !important; max-width:100% !important;}
iframe {border:0 !important; display:block !important;}
</style>
""", unsafe_allow_html=True)

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
html,body,#stage{
  margin:0;
  width:100%;
  height:100%;
  overflow:hidden;
  background:#01060b;
}
#stage{position:absolute;inset:0;}
canvas{display:block;width:100%;height:100%;}

#brand{
  position:absolute;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  z-index:20;
  pointer-events:none;
  width:min(520px,44vw);
  padding:22px 30px 28px;
  box-sizing:border-box;
  text-align:center;
  font-family:Arial,Helvetica,sans-serif;
  color:#fff;
  user-select:none;
  border-radius:50%;
  background:radial-gradient(
    ellipse at center,
    rgba(0,8,15,.94) 0%,
    rgba(0,8,15,.78) 42%,
    rgba(0,8,15,.34) 68%,
    rgba(0,8,15,0) 100%
  );
  filter:drop-shadow(0 0 22px rgba(45,190,255,.18));
}

#brand img{
  display:block;
  width:min(430px,38vw);
  max-width:100%;
  height:auto;
  margin:0 auto;
  image-rendering:auto;
  filter:drop-shadow(0 0 7px rgba(255,255,255,.18));
}

#brand .cyan-rule{
  width:138px;
  height:3px;
  margin:12px auto 13px;
  background:#55e4ff;
  border-radius:99px;
  box-shadow:
    0 0 6px rgba(85,228,255,.95),
    0 0 18px rgba(85,228,255,.55);
}

#brand .smarter{
  font-size:clamp(17px,1.7vw,24px);
  line-height:1.1;
  font-weight:800;
  letter-spacing:.22em;
  padding-left:.22em;
  color:#ffffff;
  white-space:nowrap;
  text-shadow:0 0 12px rgba(220,250,255,.48);
}

#brand .extra{
  margin-top:12px;
  font-size:clamp(15px,1.45vw,21px);
  line-height:1.1;
  font-weight:800;
  letter-spacing:.12em;
  padding-left:.12em;
  color:#eafaff;
  white-space:nowrap;
  text-shadow:
    0 0 7px rgba(190,240,255,.9),
    0 0 18px rgba(60,205,255,.62);
}

@media (max-width:700px){
  #brand{width:92vw;padding:12px 12px 18px;}
  #brand img{width:min(380px,76vw);}
  #brand .cyan-rule{width:90px;height:2px;}
}
</style>
</head>
<body>
<div id="stage">
  <div id="brand" aria-label="36 Presents — Smarter Media — Data AI Performance">
    <img src="data:image/png;base64,LOGO_DATA" alt="36 Presents">
    <div class="cyan-rule"></div>
    <div class="smarter">SMARTER MEDIA</div>
    <div class="extra">DATA • AI • PERFORMANCE</div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){
  const stage = document.getElementById("stage");
  if(!window.THREE) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(38, 1, .1, 100);
  camera.position.z = 6.25;

  const renderer = new THREE.WebGLRenderer({
    antialias:true,
    alpha:true,
    powerPreference:"high-performance"
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setClearColor(0x000000, 0);
  stage.appendChild(renderer.domElement);

  const globe = new THREE.Group();
  scene.add(globe);

  // Dense particle globe with brighter edge definition.
  const count = 7600;
  const pos = new Float32Array(count * 3);

  for(let i=0;i<count;i++){
    const z = Math.random()*2 - 1;
    const a = Math.random()*Math.PI*2;
    const rr = Math.sqrt(1-z*z);
    const radius = 1.68 + (Math.random() < .82 ? Math.random()*.035 : Math.random()*.09);

    pos[i*3]   = radius*rr*Math.cos(a);
    pos[i*3+1] = radius*z;
    pos[i*3+2] = radius*rr*Math.sin(a);
  }

  const pg = new THREE.BufferGeometry();
  pg.setAttribute("position", new THREE.BufferAttribute(pos,3));

  const particles = new THREE.Points(
    pg,
    new THREE.PointsMaterial({
      color:0xbceeff,
      size:.0125,
      transparent:true,
      opacity:.82,
      depthWrite:false,
      blending:THREE.AdditiveBlending
    })
  );
  globe.add(particles);

  // Bright network nodes.
  const nodeCount = 135;
  const nodePos = new Float32Array(nodeCount*3);
  const nodeVecs = [];

  for(let i=0;i<nodeCount;i++){
    const z = Math.random()*2 - 1;
    const a = Math.random()*Math.PI*2;
    const rr = Math.sqrt(1-z*z);
    const radius = 1.695;
    const v = new THREE.Vector3(
      radius*rr*Math.cos(a),
      radius*z,
      radius*rr*Math.sin(a)
    );
    nodeVecs.push(v);
    nodePos[i*3]=v.x;
    nodePos[i*3+1]=v.y;
    nodePos[i*3+2]=v.z;
  }

  const ng = new THREE.BufferGeometry();
  ng.setAttribute("position", new THREE.BufferAttribute(nodePos,3));

  globe.add(new THREE.Points(
    ng,
    new THREE.PointsMaterial({
      color:0xffffff,
      size:.034,
      transparent:true,
      opacity:.95,
      depthWrite:false,
      blending:THREE.AdditiveBlending
    })
  ));

  // Connect nearby nodes to create a digital/network feel.
  const linePositions = [];
  for(let i=0;i<nodeVecs.length;i++){
    let nearest = -1;
    let best = Infinity;
    for(let j=0;j<nodeVecs.length;j++){
      if(i===j) continue;
      const d = nodeVecs[i].distanceTo(nodeVecs[j]);
      if(d < best){ best=d; nearest=j; }
    }
    if(nearest >= 0 && best < .55){
      linePositions.push(
        nodeVecs[i].x,nodeVecs[i].y,nodeVecs[i].z,
        nodeVecs[nearest].x,nodeVecs[nearest].y,nodeVecs[nearest].z
      );
    }
  }

  const lg = new THREE.BufferGeometry();
  lg.setAttribute("position", new THREE.Float32BufferAttribute(linePositions,3));

  globe.add(new THREE.LineSegments(
    lg,
    new THREE.LineBasicMaterial({
      color:0x46cfff,
      transparent:true,
      opacity:.20,
      depthWrite:false,
      blending:THREE.AdditiveBlending
    })
  ));

  function orbit(rx,ry,rz,scaleY,opacity,speed){
    const curve = new THREE.EllipseCurve(
      0,0,2.12,.78*scaleY,0,Math.PI*2,false,0
    );
    const pts = curve.getPoints(260).map(p=>new THREE.Vector3(p.x,p.y,0));
    const g = new THREE.BufferGeometry().setFromPoints(pts);
    const m = new THREE.LineBasicMaterial({
      color:0x6ddfff,
      transparent:true,
      opacity:opacity,
      depthWrite:false,
      blending:THREE.AdditiveBlending
    });
    const line = new THREE.LineLoop(g,m);
    line.rotation.set(rx,ry,rz);
    line.userData.speed=speed;
    globe.add(line);
    return line;
  }

  const orbits = [
    orbit(.85,.18,.10,1.00,.26,.009),
    orbit(1.52,-.42,-.28,.92,.15,-.007),
    orbit(.30,1.10,.72,1.08,.12,.006)
  ];

  // Sparse stars around the globe.
  const starCount = 260;
  const stars = new Float32Array(starCount*3);
  for(let i=0;i<starCount;i++){
    const a=Math.random()*Math.PI*2;
    const b=Math.acos(2*Math.random()-1);
    const r=2.15+Math.random()*1.7;
    stars[i*3]=r*Math.sin(b)*Math.cos(a);
    stars[i*3+1]=r*Math.cos(b);
    stars[i*3+2]=r*Math.sin(b)*Math.sin(a);
  }

  const sg = new THREE.BufferGeometry();
  sg.setAttribute("position",new THREE.BufferAttribute(stars,3));

  scene.add(new THREE.Points(
    sg,
    new THREE.PointsMaterial({
      color:0x4ccfff,
      size:.008,
      transparent:true,
      opacity:.28,
      depthWrite:false,
      blending:THREE.AdditiveBlending
    })
  ));

  let tx=0,ty=0,mx=0,my=0;
  let dragging=false,startX=0,startY=0,startRX=0,startRY=0;

  stage.addEventListener("pointermove",e=>{
    const r=stage.getBoundingClientRect();
    const x=(e.clientX-r.left)/r.width-.5;
    const y=(e.clientY-r.top)/r.height-.5;
    tx=x*.30;
    ty=-y*.18;

    if(dragging){
      globe.rotation.y=startRY+(e.clientX-startX)*.003;
      globe.rotation.x=startRX+(e.clientY-startY)*.003;
    }
  });

  stage.addEventListener("pointerleave",()=>{tx=0;ty=0;});

  stage.addEventListener("pointerdown",e=>{
    dragging=true;
    startX=e.clientX;
    startY=e.clientY;
    startRX=globe.rotation.x;
    startRY=globe.rotation.y;
    stage.setPointerCapture(e.pointerId);
  });

  stage.addEventListener("pointerup",e=>{
    dragging=false;
    if(stage.hasPointerCapture(e.pointerId))
      stage.releasePointerCapture(e.pointerId);
  });

  function resize(){
    const w=Math.max(1,stage.clientWidth);
    const h=Math.max(1,stage.clientHeight);
    camera.aspect=w/h;
    camera.updateProjectionMatrix();
    renderer.setSize(w,h,false);
  }

  window.addEventListener("resize",resize);
  resize();

  const clock=new THREE.Clock();

  function animate(){
    requestAnimationFrame(animate);

    const t=clock.getElapsedTime();
    mx+=(tx-mx)*.045;
    my+=(ty-my)*.045;

    if(!dragging){
      globe.rotation.x+=(my-globe.rotation.x)*.016;
      globe.rotation.y+=.00062+mx*.003;
    }

    particles.rotation.y=t*.0032;
    orbits.forEach(o=>o.rotation.z+=o.userData.speed);

    renderer.render(scene,camera);
  }

  animate();
})();
</script>
</body>
</html>
"""

html = html.replace("LOGO_DATA", logo_b64)
components.html(html, height=800, scrolling=False)


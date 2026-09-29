import streamlit as st
import streamlit.components.v1 as components

# Embedded logo asset so Streamlit Cloud does not need a separate image file.
logo_b64 = "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"

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


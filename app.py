
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="36 Presents — Interactive Sphere",
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

logo_data = "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"

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
html,body,#stage{
  margin:0;width:100%;height:100%;overflow:hidden;background:#01060b;
}
#stage{position:absolute;inset:0;}
canvas{display:block;width:100%;height:100%;}

#brand{
  position:absolute;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  z-index:10;
  pointer-events:none;
  text-align:center;
  width:190px;
  font-family:Arial,Helvetica,sans-serif;
  color:#f5fbff;
  user-select:none;
  filter:drop-shadow(0 0 14px rgba(80,190,255,.22));
}
#brand img{
  width:150px;
  height:150px;
  object-fit:contain;
  display:block;
  margin:0 auto -10px;
}
#brand .smarter{
  margin-top:0;
  font-size:10px;
  font-weight:700;
  letter-spacing:.25em;
  padding-left:.25em;
  opacity:.88;
}
#brand .extra{
  margin-top:8px;
  font-size:7px;
  font-weight:600;
  letter-spacing:.20em;
  padding-left:.20em;
  opacity:.38;
}
</style>
</head>
<body>
<div id="stage">
  <div id="brand" aria-label="36 Presents — Smarter Media">
    <img src="data:image/png;base64,LOGO_DATA_PLACEHOLDER" alt="36 Presents">
    <div class="smarter">SMARTER MEDIA</div>
    <div class="extra">DATA • AI • PERFORMANCE</div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){
  const stage=document.getElementById("stage");
  if(!window.THREE) return;

  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(40,1,.1,100);
  camera.position.z=6.4;

  const renderer=new THREE.WebGLRenderer({
    antialias:true, alpha:true, powerPreference:"high-performance"
  });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
  renderer.setClearColor(0x000000,0);
  stage.appendChild(renderer.domElement);

  const root=new THREE.Group();
  scene.add(root);

  // Particle-only sphere: no filled globe and no blue outer shell.
  const count=6000;
  const positions=new Float32Array(count*3);

  for(let i=0;i<count;i++){
    const z=Math.random()*2-1;
    const a=Math.random()*Math.PI*2;
    const r=Math.sqrt(1-z*z);
    const radius=1.58+Math.random()*0.045;
    positions[i*3]=radius*r*Math.cos(a);
    positions[i*3+1]=radius*z;
    positions[i*3+2]=radius*r*Math.sin(a);
  }

  const geo=new THREE.BufferGeometry();
  geo.setAttribute("position",new THREE.BufferAttribute(positions,3));

  const points=new THREE.Points(
    geo,
    new THREE.PointsMaterial({
      color:0x9edfff,size:0.014,transparent:true,
      opacity:0.78,depthWrite:false,blending:THREE.AdditiveBlending
    })
  );
  root.add(points);

  // Bright nodes.
  const nodes=90;
  const np=new Float32Array(nodes*3);

  for(let i=0;i<nodes;i++){
    const z=Math.random()*2-1;
    const a=Math.random()*Math.PI*2;
    const r=Math.sqrt(1-z*z);
    const radius=1.60;
    np[i*3]=radius*r*Math.cos(a);
    np[i*3+1]=radius*z;
    np[i*3+2]=radius*r*Math.sin(a);
  }

  const ng=new THREE.BufferGeometry();
  ng.setAttribute("position",new THREE.BufferAttribute(np,3));

  root.add(new THREE.Points(
    ng,
    new THREE.PointsMaterial({
      color:0xe7faff,size:0.028,transparent:true,
      opacity:0.95,depthWrite:false,blending:THREE.AdditiveBlending
    })
  ));

  function makeOrbit(rx,ry,rz,sx,sy,opacity,speed){
    const curve=new THREE.EllipseCurve(
      0,0,2.0*sx,0.70*sy,0,Math.PI*2,false,0
    );
    const pts=curve.getPoints(220).map(
      p=>new THREE.Vector3(p.x,p.y,0)
    );
    const g=new THREE.BufferGeometry().setFromPoints(pts);
    const m=new THREE.LineBasicMaterial({
      color:0x7ddcff,transparent:true,opacity:opacity,
      depthWrite:false,blending:THREE.AdditiveBlending
    });
    const line=new THREE.LineLoop(g,m);
    line.rotation.set(rx,ry,rz);
    line.userData.speed=speed;
    root.add(line);
    return line;
  }

  const orbits=[
    makeOrbit(1.05,0.20,0.18,1.0,1.0,0.22,0.012),
    makeOrbit(1.70,-0.50,-0.30,1.02,0.86,0.13,-0.009),
    makeOrbit(0.45,1.10,0.78,0.92,1.05,0.10,0.010)
  ];

  const outside=150;
  const op=new Float32Array(outside*3);
  for(let i=0;i<outside;i++){
    const a=Math.random()*Math.PI*2;
    const b=Math.acos(2*Math.random()-1);
    const r=1.95+Math.random()*1.0;
    op[i*3]=r*Math.sin(b)*Math.cos(a);
    op[i*3+1]=r*Math.cos(b);
    op[i*3+2]=r*Math.sin(b)*Math.sin(a);
  }

  const og=new THREE.BufferGeometry();
  og.setAttribute("position",new THREE.BufferAttribute(op,3));

  const outsidePoints=new THREE.Points(
    og,
    new THREE.PointsMaterial({
      color:0x55b9ed,size:0.010,transparent:true,
      opacity:0.25,depthWrite:false,blending:THREE.AdditiveBlending
    })
  );
  scene.add(outsidePoints);

  let tx=0,ty=0,mx=0,my=0;
  let dragging=false,startX=0,startY=0,startRX=0,startRY=0;

  stage.addEventListener("pointermove",function(e){
    const r=stage.getBoundingClientRect();
    const x=(e.clientX-r.left)/r.width-0.5;
    const y=(e.clientY-r.top)/r.height-0.5;
    tx=x*0.34; ty=-y*0.22;

    if(dragging){
      root.rotation.y=startRY+(e.clientX-startX)*0.003;
      root.rotation.x=startRX+(e.clientY-startY)*0.003;
    }
  });

  stage.addEventListener("pointerleave",function(){tx=0;ty=0;});

  stage.addEventListener("pointerdown",function(e){
    dragging=true;
    startX=e.clientX; startY=e.clientY;
    startRX=root.rotation.x; startRY=root.rotation.y;
    stage.setPointerCapture(e.pointerId);
  });

  stage.addEventListener("pointerup",function(e){
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

    mx+=(tx-mx)*0.045;
    my+=(ty-my)*0.045;

    if(!dragging){
      root.rotation.x+=(my-root.rotation.x)*0.018;
      root.rotation.y+=mx*0.004;
      root.rotation.y+=0.00055;
    }

    points.rotation.y=t*0.004;
    outsidePoints.rotation.y=-t*0.0015;
    orbits.forEach(o=>o.rotation.z+=o.userData.speed);

    renderer.render(scene,camera);
  }

  animate();
})();
</script>
</body>
</html>
"""

html = html.replace("LOGO_DATA_PLACEHOLDER", logo_data)
components.html(html, height=780, scrolling=False)

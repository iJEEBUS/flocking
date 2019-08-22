import Boid from "./boid";

export default function sketch(p){
    let canvas;
    let boids = [];
    let num_boids = 0;

    p.setup = () => {
      canvas = p.createCanvas(p.windowWidth, p.windowHeight);
      p.noStroke();
      for (var i = 0; i < num_boids; i++) {
        let x_pos = Math.random(100)*15;
        let y_pos = Math.random(100)*15;
        let acc = p.createVector(0, 0);
        let vel = p.createVector(Math.round(Math.random()) * 2 - 1, Math.round(Math.random()) * 2 - 1);
        let pos = p.createVector(x_pos, y_pos);
        let radius = 10;
        boids.push(new Boid(p, acc, vel, pos, radius));
        p.circle(x_pos, y_pos, radius);
        p.fill('white');
      }
    }
    
    p.mouseClicked = () => {
      let acc = p.createVector(0, 0);
      let vel = p.createVector(Math.round(Math.random()) * 2 - 1, Math.round(Math.random()) * 2 - 1);
      let pos = p.createVector(p.mouseX, p.mouseY);
      let radius = 10;
      boids.push(new Boid(p, acc, vel, pos, radius));
      p.circle(p.mouseX, p.mouseY, radius);
      p.fill('white')
    }

    p.draw = () => {
      p.background('#282c34');
      boids.forEach((boid) => {
        boid.move(boids)
        boid.display()
      })
    }
}
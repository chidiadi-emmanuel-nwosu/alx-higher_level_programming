function person (a) {
  this.a = a;
  this.greet = () => {
    console.log(`${this.a}`);
  };
}

const a = new person('a');
a.greet();

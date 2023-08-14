#!/usr/bin/node

const argsLength = process.argv.length;

if (argsLength <= 3) {
  console.log(0);
} else {
  let args = [];
  for (let i = 2; i < argsLength; i++) {
    args.push(parseInt(process.argv[i]));
  }

  args = args.sort().reverse();
  console.log(args[1]);
}

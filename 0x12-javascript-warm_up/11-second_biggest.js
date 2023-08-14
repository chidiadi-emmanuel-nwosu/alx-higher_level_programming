#!/usr/bin/node

const argsLength = process.argv.length;

if (argsLength <= 3) {
  console.log(0);
} else {
  let args = [];
  for (let i = 2; i < argsLength; i++) {
    args.push(parseInt(process.argv[i], 10));
  }

  args = args.sort((a, b) => b - a);
  console.log(args[1]);
}

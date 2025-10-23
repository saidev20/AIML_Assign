function greet(name = 'Developer') {
  const hour = new Date().getHours();
  const greeting = hour < 12 ? 'morning' : hour < 18 ? 'afternoon' : 'evening';
  return `Good ${greeting}, ${name}!`;
}

if (require.main === module) {
  const customName = process.argv[2];
  console.log(greet(customName));
}

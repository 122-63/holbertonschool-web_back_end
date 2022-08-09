export default function cleanSet(set, startString) {
  const str = [];

  if (
    typeof set !== 'object'
    || typeof startString !== 'string'
    || startString.length === 0
  ) {
    return '';
  }

  for (const element of set) {
    if (element && element.startsWith(startString)) {
      str.push(element.slice(startString.length));
    }
  }
  return str.join('-');
}

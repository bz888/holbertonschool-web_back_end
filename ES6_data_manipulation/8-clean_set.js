export default function cleanSet(set, startString) {
  if (startString === undefined) return '';

  return [...set]
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}

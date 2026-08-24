/**
 * Create a DataView backed by an ArrayBuffer and set an Int8 value at a
 * specific position.
 *
 * @param {number} length - The length of the buffer in bytes.
 * @param {number} position - The byte position to update.
 * @param {number} value - The Int8 value to store.
 * @returns {DataView} The DataView backed by the new buffer.
 */
function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  view.setInt8(position, value);
  return view;
}

export default createInt8TypedArray;

const guardrail = (mathFunction) => {
  let queue = [];

  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(err.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
};

export default guardrail;

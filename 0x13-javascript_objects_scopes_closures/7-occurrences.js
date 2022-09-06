#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  if (list.constructor === Array) {
    const len = list.length;
    let counter = 0;
    for (let i = 0; i < len; i++) {
      if (searchElement === list[i]) counter++;
    }
    return counter;
  }
};

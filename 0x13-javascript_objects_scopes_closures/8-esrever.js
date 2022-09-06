#!/usr/bin/node

exports.esrever = function (list) {
  if (list.constructor === Array) {
    const len = list.length;
    const nList = [];
    for (let i = len - 1; i >= 0; i--) nList.push(list[i]);
    return nList;
  }
};

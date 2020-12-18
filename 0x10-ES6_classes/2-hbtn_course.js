export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Name must be a Number ');
    if (typeof students !== 'object' && students.every((x) => typeof x !== 'string')) throw TypeError('Name must be a array of Strings');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('name must be a String');
    this._name = newName;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('length must be a Number');
    this._length = newLength;
  }

  set students(newStudents) {
    if (newStudents.constructor !== Array && newStudents.every((el) => typeof el === 'string')) { throw TypeError('students must be an Array of Strings'); }
    this._students = newStudents;
  }
}

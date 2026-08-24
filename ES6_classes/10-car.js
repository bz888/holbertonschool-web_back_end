export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const clonedCar = this.constructor[Symbol.species];
    return new clonedCar(this._brand, this._motor, this._color);
  }
}

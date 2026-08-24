import ClassRoom from "./0-classroom.js";

const initializeRooms = () => {
    let classRooms = [
        new ClassRoom(19), 
        new ClassRoom(20), 
        new ClassRoom(34)
    ]

    return classRooms;
}

export default initializeRooms;

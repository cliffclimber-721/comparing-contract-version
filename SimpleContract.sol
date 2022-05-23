// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.7.0;

contract simpleContract {
    constructor() public {}
    uint256 storedData;

    function setData(uint256 x) public {
        storedData = x;
    }
    function getData() public view returns (uint256 retVal){
        return storedData;
    }
}
pragma solidity 0.4.0;

contract SimpleStorage2 {
    uint storedData2;

    function set(uint x) public {
        storedData2 = x;
    }

    function get() public constant returns (uint) {
        return storedData2;
    }
}
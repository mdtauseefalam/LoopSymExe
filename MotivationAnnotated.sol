// SPDX-License-Identifier: MIT
pragma solidity ^0.4.18;

contract ArithmeticOverflow {
    uint8 public result = 2;

    //@pre: result == 2 && 1 <= i && i <= n
    //@post: result == 2 * 2^n 
    function computeMultiplication(uint8 n) external returns (uint8) {
        for (uint8 i = 1; i <= n; i++) {
            result = result * 2;
        }
        return result;
    }
}
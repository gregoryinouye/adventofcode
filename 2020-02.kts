#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/2
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readPasswords(): List<String> {
    return FileReader("./2020-02.txt").readLines()
}

val input = readPasswords()

var validCount = 0

for (passwordLine in input) { 
    val (minString, maxString, characterString, _, password) = passwordLine.split("-", " ", ":")
    val min = minString.toInt()
    val max = maxString.toInt()
    val character = character[0]
    val count: Int = password.filter { it == character }.count()
    if (count >= min && count <= max) validCount++
}

println(validCount)
// 603

/**
 * Part 2
 */

 validCount = 0

for (passwordLine in input) { 
    val (firstString, secondString, character, _, password) = passwordLine.split("-", " ", ":")
    val firstPosition = firstString.toInt()
    val secondPosition = secondString.toInt()
    val character = character[0]

    if ((password[firstPosition - 1] == character) xor (password[secondPosition - 1] == character)) validCount++
}

println(validCount)
// 403

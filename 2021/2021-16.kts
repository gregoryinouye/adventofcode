#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/16
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.util.PriorityQueue

fun readInput(): List<String> {
    return FileReader("./2021-16.txt").readLines()
}

val input = readInput()
    .map { it.toList().map { it.toString() }.map { getHexadecimalBinary(it) }.joinToString("") }
    .also(::println)

fun getHexadecimalBinary(hex: String): String {
    return when (hex) {
        "0" -> "0000"
        "1" -> "0001"
        "2" -> "0010"
        "3" -> "0011"
        "4" -> "0100"
        "5" -> "0101"
        "6" -> "0110"
        "7" -> "0111"
        "8" -> "1000"
        "9" -> "1001"
        "A" -> "1010"
        "B" -> "1011"
        "C" -> "1100"
        "D" -> "1101"
        "E" -> "1110"
        "F" -> "1111"
        else -> throw RuntimeException("unexpected hexadecimal $hex")
    }
}

fun getVersion(packet: String): Int {
    return packet.take(3).toInt(2)
}

fun getTypeId(packet: String): Int {
    return packet.substring(3, 6).toInt(2)
}

fun getLiteralValue(packet: String): Pair<Int, String> {
    val binaryNumber = packet.substring(6)

    val binaryString = StringBuilder()
    var index = 0

    for (i in 0..binaryNumber.length - 1 step 5) {
        println("i: $i, binaryNumber: $binaryNumber, binaryString: $binaryString")
        binaryNumber.substring(i + 1, i + 5)
            .also { binaryString.append(it) }
        if (binaryNumber[i] == '0') {
            index = i + 5
            break
        }
    }

    return Pair(binaryString.toString().toInt(2), binaryNumber.substring(index))
}

fun getLengthTypeId(packet: String): String {
    return packet.substring(6, 7)
}

fun getLengthField(packet: String, lengthTypeId: String): Int {
    return when (lengthTypeId) {
        "0" -> packet.substring(7, 22)
        "1" -> packet.substring(7, 18)
        else -> throw RuntimeException("unexpected length type id: $lengthTypeId")
    }.toInt(2).also { println("lengthfield: $it") }
}

val versions = mutableListOf<Int>()

fun readPacket(packet: String) {
    println("packet: $packet")
    if (packet.all { it == '0' }) return

    val version = getVersion(packet)
        .also { versions.add(it) }

    val typeId = getTypeId(packet)

    when (typeId) {
        4 -> {
            val (literal, packetRemaining) = getLiteralValue(packet)
            readPacket(packetRemaining)
        }
        0, 1, 2, 3, 5, 6 -> {
            val lengthTypeId = getLengthTypeId(packet)
            when {
                lengthTypeId == "0" -> {
                    val subpacketLength = getLengthField(packet, lengthTypeId)
                    readPacket(packet.substring(22))
                    readPacket(packet.substring(22 + subpacketLength))
                }
                else -> {
                    val numberOfSubpackets = getLengthField(packet, lengthTypeId)
                    readPacket(packet.substring(18))
                }
            }
        }
        else -> throw RuntimeException("unexpected typeId $typeId")
    }
}

readPacket(input.first())

versions.also(::println)

// 38006F45291200 -> versions [1, 6, 2] = 9
// EE00D40C823060 -> versions [7, 2, 4, 1] = 14
// 8A004A801A8002F478 -> versions [4, 1, 5, 6] = 16
// 620080001611562C8802118E34 -> versions [3, 0, 0, 5, 1, 0, 3, 1, 0, 3] = 12 // wrong i get 16
// C0015000016115A2E0802F182340 -> versions [6, 0, 0, 6, 4, 7, 0, 4, 7, 0] = 23 // wrong i get 34
// A0016C880162017C3686B18A3D4780 -> versions [5, 1, 3, 7, 6, 5, 2, 2] = 31

/**
 * Part 2
 */

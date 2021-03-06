/**
 * 
 * Copyright [2016] [Bilal Ali]
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software distributed under 
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
 *  ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and limitations under the License.
 */
package org.uclab.mm.dcl.llm.exception;

/**
 * User defined exception for multiple values.
 * @author Rizvi
 */
public class MultipleValuesException extends Exception{
 MultipleValuesException(String s){
  super(s);
 }
 /**
  * The method return appropriate exception message.
  * @return 
  */
 public String toString()
 {
  return "Database is notreachable, kindly try little later";
 }
} 

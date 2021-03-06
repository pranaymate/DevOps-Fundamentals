<div class="checkBoxList">
[#assign itemCount = 0/]
[#if parameters.list??]
    [@ww.iterator value="parameters.list"]
        [#assign itemCount = itemCount + 1/]
        [#if parameters.listKey??]
            [#assign itemKey = stack.findValue(parameters.listKey)/]
        [#else]
            [#assign itemKey = stack.findValue('top')/]
        [/#if]
        [#if parameters.listValue??]
            [#assign itemValue = stack.findString(parameters.listValue)/]
        [#else]
            [#assign itemValue = stack.findString('top')/]
        [/#if]
<input type="checkbox" name="${parameters.name?html}" value="${itemKey?html}" id="${parameters.name?html}-${itemCount}"[#rt/]
        [#if tag.contains(parameters.nameValue, itemKey)]
 checked="checked"[#rt/]
        [/#if]
        [#if parameters.disabled!false]
 disabled="disabled"[#rt/]
        [#elseif parameters.disabledList??]
            [#if tag.contains(stack.findValue(parameters.disabledList), itemKey)]
 disabled="disabled"[#rt/]
            [/#if]
        [/#if]
        [#if parameters.title??]
 title="${parameters.title?html}"[#rt/]
        [/#if]
        [#include "/${parameters.templateDir}/simple/scripting-events.ftl" /]
/>
<label for="${parameters.name?html}-${itemCount}" class="checkboxLabel">${itemValue?html}</label> <br/>
    [/@ww.iterator]
[#else]
  &nbsp;
[/#if]
</div>
<input type="hidden" name="checkBoxFields" value="${parameters.name?html}" />  


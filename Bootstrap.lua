local addonName = ...

local function registerDictionary()
  local addon = WordHunterWoW_Addon
  if not addon or not addon.RegisterDictionaryProvider or type(WordHunterWoW_Dictionary_IT) ~= "table" then return end
  addon.RegisterDictionaryProvider("itIT", addonName, WordHunterWoW_Dictionary_IT)
end

local events = CreateFrame("Frame")
events:RegisterEvent("ADDON_LOADED")
events:SetScript("OnEvent", function(_, _, loaded)
  if loaded == addonName then registerDictionary() end
end)
registerDictionary()

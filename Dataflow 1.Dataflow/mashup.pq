[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared #"departments csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "33bc9708-5f6f-4292-a9da-d0b031f807eb"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "64e99a1c-7921-4899-a803-8c9ea0b0def2"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "departments.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 3", [Delimiter = ",", Columns = 4, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"department_id", Int64.Type}, {"department_name", type text}, {"manager", type text}, {"location", type text}})
in
  #"Changed column type";
shared #"employees csv" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "33bc9708-5f6f-4292-a9da-d0b031f807eb"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "64e99a1c-7921-4899-a803-8c9ea0b0def2"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "employees.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 3", [Delimiter = ",", Columns = 5, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"employee_id", Int64.Type}, {"name", type text}, {"department_id", Int64.Type}, {"hire_date", type date}, {"salary", Int64.Type}})
in
  #"Changed column type";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Merge_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared Merge = let
  Source = Table.NestedJoin(#"employees csv", {"department_id"}, #"departments csv", {"department_id"}, "departments csv", JoinKind.LeftOuter),
  #"Expanded departments csv" = Table.ExpandTableColumn(Source, "departments csv", {"department_id", "department_name", "manager", "location"}, {"department_id.1", "department_name", "manager", "location"}),
  #"Split column by delimiter" = Table.SplitColumn(#"Expanded departments csv", "name", Splitter.SplitTextByDelimiter(" "), {"name.1", "name.2"}),
  #"Renamed columns" = Table.RenameColumns(#"Split column by delimiter", {{"name.1", "First_name"}, {"name.2", "Last_name"}}),
  #"Choose columns" = Table.SelectColumns(#"Renamed columns", {"employee_id", "First_name", "salary", "department_name", "location"})
in
  #"Choose columns";
shared Merge_DataDestination = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false, EnableFolding = false, HierarchicalNavigation = true, EnableVorder = true, OutputMetadataRefresh = true]),
  Navigation_1 = Pattern{[workspaceId = "."]}[Data],
  Navigation_2 = Navigation_1{[lakehouseName = "Medallion_lakehouse"]}[Data],
  Navigation_3 = Navigation_2{[Id = "dbo", ItemKind = "Schema"]}[Data],
  TableNavigation = Navigation_3{[Id = "Mergetavant2", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
